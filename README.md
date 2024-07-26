# Socket-Programming-Tool

## Project Description

The Socket Programming Tool is a comprehensive utility designed to facilitate various network-related tasks using Python's socket programming capabilities. It includes functionalities for scanning open ports, grabbing server banners, and setting up TCP/UDP servers and clients. Additionally, it features a simple chat application for multiple clients to communicate through a server. This tool is intended for educational purposes, allowing users to understand and experiment with different aspects of socket programming.


## Features

1. **Port Scanner**: Scans a target IP address for open ports within a specified range.
2. **Banner Grabber**: Connects to a specified IP address and port to retrieve the server's banner message.
3. **TCP Server**: Sets up a TCP server to accept and display messages from clients.
4. **TCP Client**: Connects to a TCP server and sends messages.
5. **UDP Server**: Sets up a UDP server to receive and display messages from clients.
6. **UDP Client**: Sends messages to a UDP server.
7. **Chat Server**: Facilitates communication between multiple clients in a chat room setting.
8. **Chat Client**: Connects to a chat server to send and receive messages.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/salmanfareeth/Socket-Programming-Tool.git
    cd Socket-Programming-Tool
    ```

2. **Install the required Python module:**
    ```bash
    pip install socket
    pip install threading
    ```

## Usage

1. **Port Scanner:**
   ```py
   python socketprogram.py port_scanner <target_ip> <start_port> <end_port>
   Example: python socketprogram.py port_scanner 127.0.0.1 1 1024
   ```
2. **Banner Grabber:**
   ```py
   python socketprogram.py banner_grabber <target_ip> <target_port>
   Example: python socketprogram.py banner_grabber 127.0.0.1 80
   ```

3. **TCP Server:**
   ```py
   python socketprogram.py tcp_server <host> <port>
   Example: python socketprogram.py tcp_server 127.0.0.1 9999
   ```

4. **TCP Client:**
   ```py
   python socketprogram.py tcp_client <host> <port> <message>
   Example: python socketprogram.py tcp_client 127.0.0.1 9999 "Hi from Syed, TCP Server!"
   ```

5. **UDP Server:**
   ```py
   python socketprogram.py udp_server <host> <port>
   Example: python socketprogram.py udp_server 127.0.0.1 9999
   ```

6. **UDP Client:**
   ```py
   python socketprogram.py udp_client <host> <port> <message>
   Example: python socketprogram.py udp_client 127.0.0.1 9999 "Hi from Syed, UDP Server!"
   ```

7. **Chat Server:**
   ```py
   python socketprogram.py chat_server <host> <port>
   Example: python socketprogram.py chat_server 127.0.0.1 9999
   ```
   
8. **Chat Client:**
   ```py
   python socketprogram.py chat_client <host> <port>
   Example: python socketprogram.py chat_client 127.0.0.1 9999
   ```

## Developer Note

Tool developed and maintained by salmanfareeth.
This tool is in beta version.

## Disclaimer

DISCLAIMER: This tool is for learning and educational purposes only. Using it without proper authorization is illegal. Always ensure you have permission to test on the network you are working with.
