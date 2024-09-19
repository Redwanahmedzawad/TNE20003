import socket

# Define server IP and port
server_ip = '127.0.0.1'
server_port = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Messages to send to the server
messages_to_send = [
    "TNE20003!",
    "sgsdgsgdg."
]

# Send the messages to the server
for message_to_send in messages_to_send:
    client_socket.sendto(message_to_send.encode('utf-8'), (server_ip, server_port))

    # Receive the server's response
    response, _ = client_socket.recvfrom(1024)

    # Convert and process the response
    response_message = response.decode('utf-8')
    response_parts = response_message.split(':')

    if len(response_parts) == 3 and response_parts[0] == 'TNE20003' and response_parts[1] == 'A':
        # Received an acknowledgment response
        received_message = response_parts[2]
        print(f"TNE20003: {received_message}")
    elif len(response_parts) == 3 and response_parts[0] == 'TNE20003' and response_parts[1] == 'E':
        # Received an error response
        error_message = response_parts[2]
        print(f"TNE20003: {error_message}")
    else:
        print("Invalid response received")

# Close the client socket
client_socket.close()
