import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                # Broadcast the message to all clients
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()

# Function to broadcast a message to all clients except the sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

print("Server started. Waiting for connections...")

clients = []

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    clients.append(client_socket)
    # Start a new thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()