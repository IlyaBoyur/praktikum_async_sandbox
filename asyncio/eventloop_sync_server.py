import logging
import sys
from socket import AF_INET, SOCK_STREAM, socket

from core import NewTask, Scheduler

logger = logging.getLogger(__name__)


def handle_client(client, addr):
    logger.info("Connection from %s", addr)
    while True:
        data = client.recv(65536)
        if not data:
            break
        client.send(data)
        yield
    logger.info("Client closed")
    client.close()


def server(port):
    logger.info("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    try:
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))
        while True:
            yield
    finally:
        sock.close()


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))

    scheduler = Scheduler()
    scheduler.add_task(server(8000))
    scheduler.event_loop()
