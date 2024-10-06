import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("localhost", 12345))

server_socket.listen(2)

print("Server started. Waiting for a connection...")

connection, address = server_socket.accept()
print("Connected with Client ", address)

while True:
    message = connection.recv(1024).decode()
    if not message:
        break
    print("Client:", message)
    
    response = input("Server: ")
  
    connection.sendall(response.encode())

connection.close()