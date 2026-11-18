import socket
import time
import sys

if len(sys.argv) != 3:
    print("Usage: python3 tcp_round_trip_client.py <host> <port>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

start = time.perf_counter()

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall(b"x")
    sock.recv(1)

end = time.perf_counter()

elapsed_ms = (end - start) * 1000

print(f"Round-trip time: {elapsed_ms:.3f} ms")
