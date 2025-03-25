import socket  # Import the socket module for network communication

# === CONFIGURATION ===
HOST = "0.0.0.0"  # Listen on all available network interfaces (WiFi and Ethernet)
PORT = 5000       # The same port as in client.py (ensure it's not used by another program)


# === CREATE A SOCKET ===
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket

try:
    # Bind the socket to the specified IP and port
    server.bind((HOST, PORT))

    # Start listening for incoming connections (allow 1 client at a time)
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    # === WAIT FOR A CLIENT TO CONNECT ===
    conn, addr = server.accept()  # Accept an incoming connection
    print(f"Connected by {addr}")  # Print the Jetson Nano's IP address

    # === RECEIVE DATA LOOP ===
    while True:
        # Receive data from the Jetson Nano (max 1024 bytes per message)
        data = conn.recv(1024)

        # If no data is received, assume the client disconnected
        if not data:
            print("Client disconnected")
            break

        # Decode received bytes to a string and print the message
        print(f"Received: {data.decode()}")

except Exception as e:
    print(f"Server error: {e}")

finally:
    # Close the socket when done
    conn.close()
    server.close()
    print("Server stopped")
