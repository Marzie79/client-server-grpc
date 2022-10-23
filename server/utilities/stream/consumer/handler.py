from django.conf import settings


class Handler:
    """This is a class about handling all consumed tasks."""

    def task(self, routing_key: str, body):
        """Set the received message into proper method.

        Parameter:
            routing_key (str): The name of the routing.
            body: The content that published.
        """
        getattr(Handler, self.__method(key=routing_key))(body)

    @staticmethod
    def __method(key: str):
        """Select a suitable method based on key.

        Parameters:
            key: It is the routing key.
        """
        return {
            settings.STREAM_INFO.get(
                "CLIENT_SERVICE_SEND_LOG_ROUTING_KEY"
            ): "send_log"
        }.get(key)

    @staticmethod
    def send_log(body):
        """Send log.logstash 

        Parameter:
            body: The content that published.
        """
