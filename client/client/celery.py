import os
from celery import Celery

from django.conf import settings

from utilities.stream.consumer.client_consumer import ClientConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'client.settings')

app = Celery('client')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_default_exchange = settings.STREAM_INFO.get(
    'CLIENT_SERVICE_EXCHANGE'
)
app.conf.task_default_routing_key = settings.STREAM_INFO.get(
    'CLIENT_SERVICE_DEFAULT_ROUTING_KEY'
)

app.steps['consumer'].add(ClientConsumer)
