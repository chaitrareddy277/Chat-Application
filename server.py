import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()
print("Server started. Waiting for connections...")
client_socket, address = server.accept()
print("Connected with", address)
while True:
    message = client_socket.recv(1024).decode()
    if message.lower() == "exit":
        break
    print("Client:", message)
    reply = input("You: ")
    client_socket.send(reply.encode())
client_socket.close()
server.close()