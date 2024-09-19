import socket

# Define the target server and port
server = "w.google.com"
port = 80  # Default HTTP port

# Create a socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# Send an HTTP 1.0 GET request for the home page
request = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"
s.sendall(request.encode())

# Receive and print the response from the server
response = b""
while True:
    data = s.recv(1024)
    if not data:
        break
    response += data

# Close the socket
s.close()

# Print the response (HTML content)
print(response.decode("utf-8"))
"""
content = response.decode("utf-8")
with open("page.html","w") as file:
    file.write(content)
print("html created")
"""