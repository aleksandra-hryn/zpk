#Wytworzenie instancji consumera zadań

import pika
import time
import os
import json

rabbit_host = "localhost"
rabbit_port = 8081
queue_name = "task_queue"

def callback(ch, method, properties, body):
    task = json.loads(body.decode("utf-8"))
    task_name = task["name"]
    print(f"[{os.getpid()}] Podejmuję {task_name}. Status 'in_progress'")
    time.sleep(30)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"[{os.getpid()}] Zakończono {task_name}. Status 'done'")

def run_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, port=rabbit_port)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1) #jeden na raz
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    print(f"Consumer {os.getpid()} uruchomiony. Nasłuchuje kolejki {queue_name}")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(f"[{os.getpid()}] Zatrzymanie konsumenta")
        channel.stop_consuming()
    finally:
        connection.close()

if __name__ == "__main__":
    run_consumer()

#ctrl + c ubija dany terminal