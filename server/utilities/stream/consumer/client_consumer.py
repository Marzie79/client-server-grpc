import json
import logging
from datetime import datetime
from kombu import Consumer
from celery import bootsteps

from .queues import Queues
from .handler import Handler

logger = logging.getLogger(__name__)


class ClientConsumer(bootsteps.ConsumerStep):
    """ClientConsumer that starts a message consumer."""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        queues_ = Queues()
        self.handler_obj = Handler()
        self.queues = [queues_.send_log()]

    def get_consumers(self, channel):
        """Make a consumer instance. """
        return [
            Consumer(channel=channel,
                     queues=self.queues,
                     callbacks=[self.receive],
                     accept=['json'])
        ]

    def receive(self, body, message):
        """Handle all data that received based on routing key.

        Parameters:
            body: The content that published.
            message:
        """
        try:
            print(
                f'Received a message from: {message.delivery_info.get("routing_key")}')
            print(message.delivery_info.get("routing_key"))
            self.handler_obj.task(
                routing_key=message.delivery_info.get("routing_key"),
                body=json.loads(body))
            message.ack()
            print(f'Sent the related task.')
        except Exception as Error:
            message = f"An error occurred in the ClientConsumer" \
                      f" for body: {body} at {datetime.now()}..." \
                      f" {str(Error)}"
            logger.exception(message)
