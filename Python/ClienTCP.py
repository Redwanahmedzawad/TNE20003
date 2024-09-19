import socket


s_host = 'localhost'
s_port = 12345

# Create a socket object
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
c_socket.connect((s_host, s_port))

while True:
    msg = input("Enter a message to send to the server: ")
    c_socket.send(msg.encode("utf-8"))  # Send the message to the server
    data = c_socket.recv(1024)  # Receive the response from the server
    print("Received from server:", data.decode())

# Close the socket when done
c_socket.close()
