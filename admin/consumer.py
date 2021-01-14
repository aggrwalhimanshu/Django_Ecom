import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","admin.settings")
django.setup()

from products.models import Products

params= pika.URLParameters('amqps://ymwbfiit:a8YNm4mM33k_SljOU5qTnl0-ORcdso1Q@beaver.rmq.cloudamqp.com/ymwbfiit')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id= json.loads(body)
    print(id)
    product=Products.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()