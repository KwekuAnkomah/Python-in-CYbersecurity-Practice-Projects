import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5555))
print("Connecting!....")
s.send(b"GET / HTTP/1.1\r\nHost:127.0.0.1\r\n\r\n")
response = s.recv(4096)
print(response.decode())