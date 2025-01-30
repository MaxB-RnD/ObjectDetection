import socket  # Import the socket module to enable network communication
import time    # Import time module to simulate periodic data sending

# === CONFIGURATION ===
HOST = "192.168.0.116" # REPLACE with PC's IPv4 address
PORT = 5000            # Must match the server's listening port


# === CREATE A SOCKET ===
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
try:
    # Attempt to connect to the server (PC)
    client.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    # === CONTINUOUS DATA SENDING LOOP ===
    while True:
        # Simulated sensor data (replace with real sensor data if needed)
        message = f"Sensor data: {time.time()}"  # Current timestamp as dummy data

        # Send data to the server (encode to bytes since sockets transmit bytes)
        client.sendall(message.encode())

        # Print confirmation in Jetson Nano's terminal
        print(f"Sent: {message}")

        # Wait 10 seconds before sending the next message
        time.sleep(10)

except Exception as e:
    print(f"Connection error: {e}")

finally:
    # Close the socket connection when the program ends
    client.close()
    print("Connection closed")