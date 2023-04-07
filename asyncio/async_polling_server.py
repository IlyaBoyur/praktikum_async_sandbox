import json
import logging
import platform
import re
import selectors
import socket
import sys
import uuid
from datetime import datetime

HOST, PORT = "", 8000  # Порт сервера


logger = logging.getLogger(__name__)


def determine_time_of_a_day():
    now = datetime.now().time()
    hour = now.hour
    if 5 < hour < 12:
        return "morning"
    if 12 < hour < 18:
        return "afternoon"
    if 18 < hour < 24:
        return "evening"
    return "night"


def get_system_info():
    try:
        info = {
            "platform": platform.system(),
            "platform-release": platform.release(),
            "platform-version": platform.version(),
            "architecture": platform.machine(),
            "hostname": socket.gethostname(),
            "ip-address": socket.gethostbyname(socket.gethostname()),
            "mac-address": ":".join(re.findall("..", "%012x" % uuid.getnode())),
            "processor": platform.processor(),
            # "ram": str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        }
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def new_connection(selector: selectors.BaseSelector, sock: socket.socket):
    new_conn, address = sock.accept()
    logger.info("accepted new_conn from %s", address)
    new_conn.setblocking(False)
    selector.register(new_conn, selectors.EVENT_READ, read_callback)
    new_conn.send(
        f"Good {determine_time_of_a_day()}!\n"
        f"Server on {socket.gethostbyname(socket.gethostname())}"
        f" is ready for requests...\n".encode("utf-8")
    )


def read_callback(selector: selectors.BaseSelector, sock: socket.socket):
    data = sock.recv(1024)
    try:
        data = data.decode().strip()
    except Exception as e:
        logger.exception(e)
    else:
        if not data or (data == "quit"):
            logger.info("closing connection %s", sock)
            sock.send("I quit!\n".encode())
            selector.unregister(sock)
            sock.close()
        elif data == "time":
            sock.send(f"Now: {datetime.now().utcnow()}\n".encode())
        elif data == "info":
            sock.send(f"{get_system_info()}\n".encode())
        else:
            sock.send("Unknown command\n".encode())


def run_iteration(selector: selectors.BaseSelector):
    events = selector.select()
    for key, mask in events:
        callback = key.data
        callback(selector, key.fileobj)


def serve_forever():
    """
    Метод запускает сервер на постоянное прослушивание новых сообщений
    """
    with selectors.SelectSelector() as selector:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            server_socket.setblocking(False)
            logger.info("Server started on port %s", PORT)

            # Читается это выражение так: «Зарегистрировать каждое событие получения новых данных
            # по серверному сокету и вызвать функцию new_connection».
            # Другими  словами, каждый раз, когда к серверу отправляют новую пачку данных
            # и её получает ОС, она отправляет событие в программу,
            # а та вызывает функцию new_connection.
            selector.register(server_socket, selectors.EVENT_READ, new_connection)

            while True:
                run_iteration(selector)


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    serve_forever()
