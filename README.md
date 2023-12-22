# Simple TCP Chat Application

This repository contains a simple TCP chat application implemented in Python. It consists of two main scripts: a server (`server.py`) and a client (`client.py`). The server script sets up a TCP server that multiple clients can connect to and exchange messages. The client script allows users to connect to the server and participate in the chat.

 Features

- TCP Server: Handles multiple client connections and relays messages between clients.
- TCP Client: Connects to the TCP server, sends messages, and receives messages from other clients.

 Usage

# Server

1. Run the server script on a machine by executing `python server.py`.
2. The server will start and listen for incoming client connections.

# Client

1. Run the client script on a machine by executing `python client.py`.
2. Enter the server's IP address and port number to connect.
3. Once connected, type messages and press Enter to send them to the chat.

# Server Script (`server.py`)

The server script sets up a TCP server that listens for incoming connections from clients. When a client sends a message, the server broadcasts it to all other connected clients.

Key Functions:
- `broadcast_message`: Sends a received message to all clients except the sender.
- `handle_client`: Manages a client connection, receives messages, and coordinates with `broadcast_message`.
- `start_tcp_server`: Initializes the server and starts listening for clients.

# Client Script (`client.py`)

The client script connects to the TCP server and allows the user to send and receive messages.

# Key Functions:
- `receive_messages`: Listens for incoming messages from the server and displays them.
- `send_messages`: Lets the user input messages and sends them to the server.
- `connect_to_tcp_server`: Connects to the server and starts the `receive_messages` and `send_messages` threads.

# Requirements

- Python 3.x
- Network access to the server (if running client and server on different machines)

# Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](#) if you want to contribute.
