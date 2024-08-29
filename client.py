import socket
import threading

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            print("An error occurred.")
            client_socket.close()
            break

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Start a thread to handle incoming messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

while True:
    message = input("You: ")
    client.send(message.encode('utf-8'))