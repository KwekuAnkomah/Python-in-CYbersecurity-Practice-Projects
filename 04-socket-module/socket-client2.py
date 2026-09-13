import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5555))
print("Connecting!....")
s.send(b"Hello Server!\r\nAre you active?...")
response = s.recv(4096)
print(response.decode())