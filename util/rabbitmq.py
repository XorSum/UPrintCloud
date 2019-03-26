import pika


def push(uri, username, passwd, content, queue_name):
    user = pika.PlainCredentials(username, passwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(uri, credentials=user))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=content,
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()
