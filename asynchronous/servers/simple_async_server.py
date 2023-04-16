import socket

HOST, PORT = "", 8888


def handle_request(request: bytes) -> bytes:
    request_data = request.decode()
    http_response = (
        f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{request_data}"""
    )
    return http_response.encode()


def serve_forever():
    # Под капотом сокеты работают с событиями операционной системы.
    # Таким образом можно создать очень много сокетов и опрашивать их по кругу каждый раз.
    # Устанавливаем TCP-соединение
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
        # Сокет использует для своей работы файловые дескрипторы,
        # но в некоторых случаях ему может не хватить объёма портов — максимум 65 535.
        # Поэтому необходимо включить опцию переиспользования:
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen()
        # Чтобы сделать сокет неблокирующим:
        listen_socket.setblocking(False)

        while True:
            client_connection, client_address = listen_socket.accept()
            with client_connection:
                request = client_connection.recv(
                    1024
                )  # Получаем информацию от клиента
                http_response = handle_request(request)
                client_connection.sendall(http_response)


if __name__ == "__main__":
    serve_forever()
