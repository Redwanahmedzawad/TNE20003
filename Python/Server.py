import socket

# Define server IP and port
server_ip = '127.0.0.1'
server_port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server IP and port
server_socket.bind((server_ip, server_port))

print(f"Server listening on {server_ip}:{server_port}")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)

    # Convert received data to string
    received_message = data.decode('utf-8')

    # Check if the received message matches the protocol header and format
    if received_message.startswith('TNE20003:'):
        # Extract the message content
        message_start = len('TNE20003:')
        message_content = received_message[message_start:]

        # Check if <message> is at least one character long
        if message_content:
            # Respond with an acknowledgment message
            acknowledgment_message = f"TNE20003:A:{message_content}"
            server_socket.sendto(acknowledgment_message.encode('utf-8'), client_address)
        else:
            # If <message> is empty, send an error message
            error_message = "Empty message received"
            error_response = f"TNE20003:E:{error_message}"
            server_socket.sendto(error_response.encode('utf-8'), client_address)
    else:
        # If the message does not match the protocol, send an error message
        error_message = "Invalid message format"
        error_response = f"TNE20003:E:{error_message}"
        server_socket.sendto(error_response.encode('utf-8'), client_address)
