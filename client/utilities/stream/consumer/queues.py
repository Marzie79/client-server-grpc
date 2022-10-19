from kombu import Queue, Exchange

from django.conf import settings


class Queues:
    """This class is about add all related stream queues."""

    @staticmethod
    def send_log():
        return Queue(
            name=settings.STREAM_INFO.get('CLIENT_SERVICE_SEND_LOG_QUEUE'),
            exchange=Exchange(settings.STREAM_INFO.get(
                'CLIENT_SERVICE_EXCHANGE'
            ), type='direct'),
            routing_key=settings.STREAM_INFO.get(
                'CLIENT_SERVICE_SEND_LOG_ROUTING_KEY'
            )
        )
