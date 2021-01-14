import pika, json

params= pika.URLParameters('amqps://ymwbfiit:a8YNm4mM33k_SljOU5qTnl0-ORcdso1Q@beaver.rmq.cloudamqp.com/ymwbfiit')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='admin', body=json.dumps(body), properties=properties)