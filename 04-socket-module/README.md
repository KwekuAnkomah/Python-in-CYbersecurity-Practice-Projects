# Sockets Fundamentals

A basic TCP client and server built from scratch using Python's socket module.

## Files
- `socket-client.py` — connects to a server, sends a GET request, receives and prints the response
- `socket-client2.py` — second client for testing multiple connections
- `socket-server.py` — listens on port 5555, accepts multiple clients in a loop, receives and sends data

## Concepts covered
- Creating TCP sockets with AF_INET and SOCK_STREAM
- Connecting to a server with connect()
- Binding and listening with bind() and listen()
- Accepting connections with accept()
- Sending and receiving bytes with send() and recv()
- Keeping a server alive with a while loop
- Difference between the listening socket and the client socket
