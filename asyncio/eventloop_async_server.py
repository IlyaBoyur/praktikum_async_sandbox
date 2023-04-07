from __future__ import annotations

import logging
import sys
from socket import AF_INET, SOCK_STREAM, socket
from typing import Tuple

from core import NewTask, Scheduler, SystemCall

logger = logging.getLogger(__name__)


# Wait for writing
class WriteWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, scheduler, task):
        fd = self.f.fileno()
        scheduler.wait_for_write(task, fd)


# Wait for reading
class ReadWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, scheduler, task):
        fd = self.f.fileno()
        scheduler.wait_for_read(task, fd)


class AsyncSocket:
    def __init__(self, sock: socket):
        self.sock = sock

    def accept(self) -> Tuple["AsyncSocket", str]:
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        return AsyncSocket(client), addr

    def send(self, buffer: bytes):
        while buffer:
            yield WriteWait(self.sock)
            len = self.sock.send(buffer)
            buffer = buffer[len:]

    def recv(self, maxbytes: int) -> bytes:
        yield ReadWait(self.sock)
        return self.sock.recv(maxbytes)

    def close(self):
        yield self.sock.close()


def handle_client(client, addr):
    logger.info("Connection from", addr)
    while True:
        data = yield from client.recv(65536)
        if not data:
            break
        yield from client.send(data)
    logger.info("Client closed")
    client.close()


def server(port):
    logger.info("Server starting")
    rawsock = socket(AF_INET, SOCK_STREAM)
    rawsock.bind(("", port))
    rawsock.listen()
    sock = AsyncSocket(rawsock)
    try:
        client, addr = yield from sock.accept()
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
