import socket

# Define host and port to listen on
import threading

HOST = 'localhost'
PORT = 12345

# Function to handle client requests
def handle_client(c_socket):

    while True:
        response = b""
        data = c_socket.recv(1024)  # Receive data from client
        if not data:
            break  # No more data from client
        response +=data
        # Process data (implement your protocol logic here)
        rp = process_data(response)
        c_socket.send(rp)  # Send response back to the client
    c_socket.close()

# Function to process received data (implement your protocol logic here)
def process_data(data):
    # Implement your logic to parse and respond to the data here
    response_str = data.decode("utf-8")

    received_message = response_str
    response = ''
    print(received_message)
    if received_message.startswith('TNE20003:'):
        # Extract the message content
        message_start = len('TNE20003:')
        message_content = received_message[message_start:]

        # Check if <message> is at least one character long
        if message_content:
            # Respond with an acknowledgment message
            acknowledgment_message = f"TNE20003:A:{message_content}"
            response = acknowledgment_message.encode("utf-8")
            return response
        else:
            # If <message> is empty, send an error message
            error_message = "Empty message received"
            error_response = f"TNE20003:E:{error_message}"
            response = error_response.encode("utf-8")
            return response
    else:
        # If the message does not match the protocol, send an error message
        error_message = "Invalid message format"
        error_response = f"TNE20003:E:{error_message}"
        response = error_response.encode("utf-8")
        return response
    # Example: echo the data back


# Create a socket object
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
s_socket.bind((HOST, PORT))

# Start listening for incoming connections
s_socket.listen(5)
print(f"Listening on {HOST}:{PORT}")

while True:
    c_socket, addr = s_socket.accept()  # Accept a new connection
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    c_handler = threading.Thread(target=handle_client, args=(c_socket,))
    c_handler.start()

