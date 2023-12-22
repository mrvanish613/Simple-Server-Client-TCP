import socket
import threading

clients = []

def broadcast_message(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address} has been established.")
    clients.append(client_socket)
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Message received from {client_address}: {message.decode()}")
            broadcast_message(message, client_socket)
    except Exception as e:
        print(f"An error occurred with client {client_address}: {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)
        print(f"Connection with {client_address} closed.")


def start_tcp_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((ip, port))
        server_socket.listen(5)
        print(f"Server listening on {ip}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    start_tcp_server('127.0.0.1', 12345)
