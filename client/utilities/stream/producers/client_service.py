import json
from kombu import Exchange, Queue

from django.conf import settings

from client.celery import app


class Client:
    @staticmethod
    def send_log(body):
        """Produces a task for sending log"""
        queue_ = Queue(
            name=settings.STREAM_INFO.get(
                "CLIENT_SERVICE_SEND_LOG_QUEUE"
            ),
            exchange=Exchange(settings.STREAM_INFO.get(
                "CLIENT_SERVICE_EXCHANGE"
            )),
            routing_key=settings.STREAM_INFO.get(
                "CLIENT_SERVICE_SEND_LOG_ROUTING_KEY"
            )
        )
        with app.producer_or_acquire(None) as producer:
            producer.publish(
                body=body,
                serializer='json',
                exchange=queue_.exchange,
                routing_key=queue_.routing_key,
                declare=[queue_],
                retry=True,
            )
            print("here")

# import json
# from utilities.stream.producers.client_service import Client
# Client.send_log(json.loads({"hello": "bye"}))