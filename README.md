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


## References

For more information on socket programming, please refer to the following resources:

1. **Python Socket Programming: Introduction and Tutorials**
   - Link: [Real Python](https://realpython.com/python-sockets/)
   - Description: Comprehensive guide on Python socket programming, covering basic to advanced concepts.

2. **Beej's Guide to Network Programming**
   - Link: [Beej's Guide](http://beej.us/guide/bgnet/)
   - Description: A well-known and highly recommended guide for learning network programming in C, which also applies to Python.

3. **Python Documentation on Sockets**
   - Link: [Python Sockets](https://docs.python.org/3/library/socket.html)
   - Description: Official Python documentation providing detailed information on the socket module.

4. **Socket Programming in Python by GeeksforGeeks**
   - Link: [GeeksforGeeks](https://www.geeksforgeeks.org/socket-programming-python/)
   - Description: Step-by-step tutorials on socket programming in Python with practical examples.

5. **Python Socket Programming Tutorial by Tutorialspoint**
   - Link: [Tutorialspoint](https://www.tutorialspoint.com/python/python_networking.htm)
   - Description: A tutorial on networking in Python, including socket programming basics and examples.

6. **Python Networking Programming Cookbook**
   - Link: [O'Reilly](https://www.oreilly.com/library/view/python-network-programming/9781785885123/)
   - Description: A cookbook that covers various network programming tasks in Python, offering practical solutions and code examples.

7. **Unix Network Programming by W. Richard Stevens**
   - Link: [Unix Network Programming](https://www.amazon.com/Unix-Network-Programming-Vol-Networking/dp/0131411551)
   - Description: A classic book on network programming that, while focused on Unix, provides fundamental concepts applicable in Python.

8. **Python for Networking and Security by José Manuel Ortega**
   - Link: [Packt Publishing](https://www.packtpub.com/product/python-for-networking-and-security/9781789952081)
   - Description: A book that dives into Python's networking and security capabilities, covering socket programming and more.


## Developer Note

Tool developed and maintained by `salmanfareeth`.
This tool is in beta version.

## Disclaimer

This tool is for learning and educational purposes only. Using it without proper authorization is illegal. Always ensure you have permission to test on the network you are working with.
