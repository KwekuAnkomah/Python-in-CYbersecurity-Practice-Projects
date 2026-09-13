import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5555))
s.listen(5)
print("Listening!....")

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address}")
    response = client_socket.recv(4096)
    print(response.decode())
    client_socket.send(b"Hello...")