#wytworzenie instancji producera zadań

import uuid
import sys
import sqlite3

db_name = 'task.db'

def init_db(con):
    with con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

def produce_task(count=1):
    con = sqlite3.connect(db_name, timeout = 30)
    try:
        init_db(con)
        with con:
            for i in range(count):
                task_id = str(uuid.uuid4())[:8] #nadaje losowe id
                task_name = f"Zadanie numer-{task_id}"
                con.execute(
                "INSERT INTO tasks (id, name, status) VALUES (?, ?, ?)",
                (task_id, task_name, "pending")
                )
    finally:
        con.close()

if __name__ == "__main__":
    tasks_to_add = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    produce_task(tasks_to_add)


