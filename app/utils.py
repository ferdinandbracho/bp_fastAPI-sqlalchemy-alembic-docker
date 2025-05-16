import json
from typing import Optional

import pika

from app.config import settings

logger = settings.get_logger(__name__)


def send_message_rabbit(rabbit_url: str, queue: str, message: dict) -> bool:
    """
    Send a message to a RabbitMQ queue.

    :param rabbit_url: URL of the RabbitMQ server.
    :param queue: Name of the queue.
    :param message: Message to send.
    :return: True if the message was sent, False otherwise.
    """
    try:
        parameters = pika.URLParameters(rabbit_url)
        with pika.BlockingConnection(parameters) as connection:
            channel = connection.channel()
            channel.queue_declare(queue=queue)
            body = json.dumps(message, indent=4, ensure_ascii=False)
            channel.basic_publish(exchange='', routing_key=queue, body=body)
            return True
    except pika.exceptions.AMQPError as e:
        logger.warn(f"Failed to send message to RabbitMQ: {e}")
        return False


def consume_message_rabbit(rabbit_url: str, queue: str) -> Optional[dict]:
    """
    Consume a message from a RabbitMQ queue.

    :param rabbit_url: URL of the RabbitMQ server.
    :param queue: Name of the queue.
    :return: Message if it was consumed, None otherwise.
    """
    try:
        parameters = pika.URLParameters(rabbit_url)
        with pika.BlockingConnection(parameters) as connection:
            channel = connection.channel()
            channel.queue_declare(queue=queue)
            method_frame, _, body = channel.basic_get(queue=queue)
            if method_frame:
                channel.basic_ack(method_frame.delivery_tag)
                return json.loads(body)
            else:
                return None
    except pika.exceptions.AMQPError as e:
        logger.warn(f"Failed to consume message from RabbitMQ: {e}")
        return None
