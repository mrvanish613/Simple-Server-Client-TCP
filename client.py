import socket
import threading

def receive_messages(client_socket, ip):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n[+] {ip}: {message}")
            else:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break


def send_messages(client_socket):
    while True:
        message = input()
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def connect_to_tcp_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, port))
        print(f"[+] Connected to server {ip}:{port}")


        receive_thread = threading.Thread(target=receive_messages, args=(client_socket, ip))
        receive_thread.start()

        send_thread = threading.Thread(target=send_messages, args=(client_socket,))
        send_thread.start()

    except Exception as e:
        print(f"Unable to connect to the server: {e}")

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 12345
    connect_to_tcp_server(ip, port)
