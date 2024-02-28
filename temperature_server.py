# temperature_server.py
import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Received data from {address}: {data.decode()}")

if __name__ == "__main__":
    server_host = "0.0.0.0"  # Listen on all available interfaces
    server_port = 5555

    start_server(server_host, server_port)
