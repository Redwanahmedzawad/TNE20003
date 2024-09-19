import socket
import argparse
from urllib.parse import urlparse
import re
import os


def extract_images(html_content):
    # Parse the HTML content to find <img> tags
    img_tags = re.findall(r'<img\s+alt="Google"\s+height="92"\s+src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp\.png"\s+style="padding:28px 0 14px"\s+width="272"\s+id="hplogo">', html_content)
    img_tofsrc = img_tags[0].split(" ")
    #print(img_tofsrc[3])
    img_src_arr = img_tofsrc[3].split('"')
    img_src = img_src_arr[1];
    # Download and save each image
    #print(img_src)
    img_url = "www.google.com" +img_src
    server = "www.google.com"
    port = 80  # Default HTTP port

    # Create a socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    # Construct a filename from the URL
    img_filename = img_url.split('/')[-1]
    print(img_url)
    request = f"GET /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

    s.sendall(request.encode())

    # Receive the response from the server
    response = b""
    while True:
        data = s.recv(8)
        if not data:
            break
        response += data

    # Close the socket
    s.close()
    header_body_separator = response.find(b"\r\n\r\n")
    response_body = response[header_body_separator + 4:]
    with open("img2.png", "wb") as f:
        try:
            f.write(response_body)
            print("write")
        except Exception as e:
            print(f"An error occurred while writing the image:")
    print(response)
    with open("img2.png", "rb") as file:
        bidat = file.read()
    # Download and save the image
    if(bidat == response):
        print("equal")
    else:
        print("Not")


    print(f"Downloaded: {img_filename}")


def main():
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

    # Extract and display the response code and message
    response_code_line = http_response.split('\r\n')[0]
    response_code_parts = response_code_line.split(' ', 2)
    response_code = response_code_parts[1]
    response_message = response_code_parts[2]
    print(f"\nResponse Code: {response_code}\nResponse Message: {response_message}")

    # Extract and display the header content as a dictionary
    header_lines = http_response.split('\r\n')[1:]
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
        # Extract and display the HTML content
        print("\nHTML Content:")
        print(response_data)
        print("\n\n\n\n")

        # Extract and download images
        extract_images(response_data)
    with open("page.html", "w") as file:
        file.write(response_str)
    print("html created")


if __name__ == "__main__":
    main()
