import socket

HOST = "0.0.0.0"
PORT = 9100

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"TCP echo server listening on port {PORT}")

    while True:
        conn, addr = server.accept()

        with conn:
            data = conn.recv(1024)

            if data:
                conn.sendall(data)
