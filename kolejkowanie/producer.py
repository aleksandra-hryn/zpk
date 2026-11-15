#wytworzenie instancji producera zadań

import pika
import uuid
import sys
import json

rabbit_host = "localhost"
rabbit_port = 8081
queue_name = "task_queue"

def produce_task(count=1):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, port=rabbit_port)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True) #deklaracja kolejki; przetrwa restart kontenera
    for i in range(count):
        task_id = str(uuid.uuid4())[:8] #nadaje losowe id
        task_data = {
            "id": task_id,
            "name": f"Zadanie numer {task_id}",
            "status": "pending"
        }
        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=json.dumps(task_data),
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent
            )
        )
    connection.close()

if __name__ == "__main__":
    tasks_to_add = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    produce_task(tasks_to_add)


