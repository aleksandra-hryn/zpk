#Wytworzenie instancji consumera zadań

import csv
import time
import os
from filelock import FileLock

file_name = 'task.csv'
lock_name = 'task.csv.lock'

def get_and_lock_task():
    if not os.path.exists(file_name):
        return None
    lock = FileLock(lock_name)
    task_to_process = None
    with lock:
        with open (file_name, mode= 'r', newline= '', encoding='utf-8') as file:
            reader = csv.reader(file)
            tasks = list(reader)
        for i, row in enumerate(tasks):
            if len(row) == 3 and row[2] == 'pending':
                task_to_process = row
                tasks[i][2] = 'in_progress'
                break #szukanie zadania pending, zmiana statusu na progress
        if task_to_process:
            with open(file_name, mode= 'w', newline= '', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(tasks) #jak jest zadanie nadpisuje plik
    return task_to_process

def task_done(task_id):
    lock = FileLock(lock_name)
    with lock:
        with open(file_name, mode= 'r', newline= '', encoding='utf-8') as file:
            reader = csv.reader(file)
            tasks = list(reader)
        for i, row in enumerate(tasks):
            if row[0] == task_id:
                tasks[i][2] = 'done'
                break
        with open(file_name, mode= 'w', newline= '', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

def run_consumer():
    print(f"Consumer o PID: {os.getpid()} uruchomiony. Czeka na zadania")
    while True:
        task = get_and_lock_task()
        if task:
            task_id, task_name, _ = task
            print(f"[{os.getpid()}] Podejmuję {task_name}. Status 'in_progress'")
            time.sleep(30)
            task_done(task_id)
            print(f"[{os.getpid()}] Zakończono {task_name}. Status 'done'")
        else:
            time.sleep(5)

if __name__ == "__main__":
    run_consumer()

#ctrl + c ubija dany terminal