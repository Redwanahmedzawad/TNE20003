import socket

# Define the target server and port
server = "www.google.com"
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

# Decode the response (HTML content)
response_str = response.decode("utf-8")

# Split the response into HTTP response, header, and HTML content
http_response, response_data = response_str.split('\r\n\r\n', 1)
http_response_lines = http_response.split('\r\n')

# Extract and display the response code and message
response_code_line = http_response_lines[0]
response_code_parts = response_code_line.split(' ', 2)
response_code = response_code_parts[1]
response_message = response_code_parts[2]
print(f"Response Code: {response_code}\nResponse Message: {response_message}")

# Extract and display the header content as a dictionary
header_lines = http_response_lines[1:]
header_dict = {}
for line in header_lines:
    key, value = line.split(': ', 1)
    header_dict[key] = value
print("\nHeader Content:")
for key, value in header_dict.items():
    print(f"{key}: {value}")

# Check if the HTTP response is not 200 (OK) and display an error message
if response_code != "200":
    print(f"\nError: HTTP Response Code {response_code}")
else:
    # Print the HTML contents to the screen
    print("\nHTML Content:")
    print(response_data)
with open("page.html", "w") as file:
    file.write(response_data)
print("html created")