from kombu import Queue, Exchange

from django.conf import settings
from utilities.singleton_meta import SingletonMeta


class Queues(metaclass=SingletonMeta):
    """This class is about add all related stream queues."""

    @staticmethod
    def profile():
        return Queue(
            name=settings.STREAM_INFO.get("COMMUNITY_SERVICE_PROFILE_QUEUE"),
            exchange=Exchange(settings.STREAM_INFO.get(
                "GENERAL_EXCHANGE"
            ), type="topic"),
            routing_key=settings.STREAM_INFO.get(
                "PROFILE_ROUTING_KEY_TOPIC"
            )
        )
