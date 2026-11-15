#wytworzenie instancji producera zadań

import csv
import uuid
import sys
from filelock import FileLock

file_name = 'task.csv'
lock_name = 'task.csv.lock'

def produce_task(count=1):
    lock = FileLock(lock_name)
    with lock:
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for i in range(count):
                task_id = str(uuid.uuid4())[:8] #nadaje losowe id
                task_name = f"Zadanie numer-{task_id}"
                writer.writerow([task_id, task_name, "pending"])

if __name__ == "__main__":
    tasks_to_add = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    produce_task(tasks_to_add)


