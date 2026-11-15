#Wytworzenie instancji consumera zadań

import time
import os
import sqlite3

db_name = 'task.db'

def get_and_lock_task():
    con = sqlite3.connect(db_name, timeout=30)
    con.isolation_level = None
    cursor = con.cursor()
    task_to_process = None
    try:
        cursor.execute("BEGIN IMMEDIATE") #inni nie mogą jednocześnei
        cursor.execute("SELECT id, name FROM tasks WHERE status = 'pending' LIMIT 1")
        row = cursor.fetchone()
        if row:
            task_id, task_name = row
            cursor.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ?",(task_id,))
            task_to_process = (task_id, task_name)
        cursor.execute("COMMIT")
    except sqlite3.Error as error:
        cursor.execute("ROLLBACK")
        print(f"[{os.getpid()}] Błąd bazy danych podczas pobierania zadania {error}")
    finally:
        con.close()
    return task_to_process

def task_done(task_id):
   con = sqlite3.connect(db_name, timeout=30)
   try:
       with con:
           con.execute("UPDATE tasks SET status = 'done' WHERE id = ?",(task_id,))
   finally:
       con.close()

def run_consumer():
    print(f"Consumer o PID: {os.getpid()} uruchomiony. Czeka na zadania")
    while True:
        task = get_and_lock_task()
        if task:
            task_id, task_name = task
            print(f"[{os.getpid()}] Podejmuję {task_name}. Status 'in_progress'")
            time.sleep(30)
            task_done(task_id)
            print(f"[{os.getpid()}] Zakończono {task_name}. Status 'done'")
        else:
            time.sleep(5)

if __name__ == "__main__":
    run_consumer()

#ctrl + c ubija dany terminal