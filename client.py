import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 12345))

print("Connected with Server. Type 'exit' to quit.")

while True:
    message = input("Client: ")
    if message.lower() == "exit":
        break
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024).decode()
    print("Server:", response)

client_socket.close()
