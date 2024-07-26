import socket
import threading
import argparse


# ASCII Art
ASCII_ART = r"""
 _____                _ _                                                                     
/  ___|              | ( )                                                                    
\ `--. _   _  ___  __| |/ ___                                                                 
 `--. \ | | |/ _ \/ _` | / __|                                                                
/\__/ / |_| |  __/ (_| | \__ \                                                                
\____/ \__, |\___|\__,_| |___/                                                                
        __/ |                                                                                 
       |___/                                                                                  
 _____            _        _    ______                                      _____           _ 
/  ___|          | |      | |   | ___ \                                    |_   _|         | |
\ `--.  ___   ___| | _____| |_  | |_/ / __ ___   __ _ _ __ __ _ _ __ ___     | | ___   ___ | |
 `--. \/ _ \ / __| |/ / _ \ __| |  __/ '__/ _ \ / _` | '__/ _` | '_ ` _ \    | |/ _ \ / _ \| |
/\__/ / (_) | (__|   <  __/ |_  | |  | | | (_) | (_| | | | (_| | | | | | |   | | (_) | (_) | |
\____/ \___/ \___|_|\_\___|\__| \_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_|   \_/\___/ \___/|_|
                                                 __/ |                                        
                                                |___/                                         
        __   _____                                                                            
       /  | |  _  |                                                                           
__   __`| | | |/' |                                                                           
\ \ / / | | |  /| |                                                                           
 \ V / _| |_\\ |_/ /                                                                           
  \_/  \___(_)___/                                                                            
  ______                                                                                      
 |______|                                                                                     
"""

# Developer and Disclaimer Notes
DEVELOPER_NOTE = """
Tool developed and maintained by Syed Salman.
This tool is in beta version.
"""

DISCLAIMER = """
DISCLAIMER: This tool is for learning and educational purposes only.
Using it without proper authorization is illegal. Always ensure you have permission to test on the network you are working with.
"""


# Port Scanner
def port_scanner(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Banner Grabber
def banner_grabber(target_ip, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, target_port))
        banner = sock.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return str(e)
    finally:
        sock.close()

# TCP Server
def tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"TCP Server listening on {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        client_socket.close()

# TCP Client
def tcp_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(message.encode())
    client_socket.close()

# UDP Server
def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        try:
            message, addr = server_socket.recvfrom(1024)
            print(f"Received message from {addr}: {message.decode()}")
        except Exception as e:
            print(f"UDP Server error: {e}")

# UDP Client
def udp_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode(), (host, port))
    client_socket.close()

# Chat Server
clients = []

def handle_client(client_socket):
    try:
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    broadcast(message, client_socket)
                else:
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.remove(client)

def chat_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Chat server listening on {host}:{port}")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                print(f"Connection from {addr}")
                clients.append(client_socket)
                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.daemon = True
                thread.start()
            except Exception as e:
                print(f"Error accepting connection: {e}")
    
    except Exception as e:
        print(f"Error starting chat server: {e}")
    
    finally:
        server_socket.close()

# Chat Client
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break
    client_socket.close()

def chat_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()
    
    try:
        while True:
            message = input()
            if message.lower() == 'quit':
                client_socket.send("User has left the chat".encode())
                break
            client_socket.send(message.encode())
    except KeyboardInterrupt:
        print("Client interrupted")
    finally:
        client_socket.close()

def main():
    print(ASCII_ART)
    print(DEVELOPER_NOTE)
    print(DISCLAIMER)

    parser = argparse.ArgumentParser(description="Syed's Socket Programming Tool")
    
    subparsers = parser.add_subparsers(dest='command', help="Commands")
    
    # Port Scanner
    parser_scanner = subparsers.add_parser('port_scanner', help="Scan a range of ports on a target IP")
    parser_scanner.add_argument('target_ip', type=str, help="Target IP address")
    parser_scanner.add_argument('start_port', type=int, help="Start port")
    parser_scanner.add_argument('end_port', type=int, help="End port")
    
    # Banner Grabber
    parser_banner = subparsers.add_parser('banner_grabber', help="Grab the banner of a service on a specified port")
    parser_banner.add_argument('target_ip', type=str, help="Target IP address")
    parser_banner.add_argument('target_port', type=int, help="Target port")
    
    # TCP Server
    parser_tcp_server = subparsers.add_parser('tcp_server', help="Start a TCP server")
    parser_tcp_server.add_argument('host', type=str, help="Host address")
    parser_tcp_server.add_argument('port', type=int, help="Port number")
    
    # TCP Client
    parser_tcp_client = subparsers.add_parser('tcp_client', help="Start a TCP client")
    parser_tcp_client.add_argument('host', type=str, help="Host address")
    parser_tcp_client.add_argument('port', type=int, help="Port number")
    parser_tcp_client.add_argument('message', type=str, help="Message to send")
    
    # UDP Server
    parser_udp_server = subparsers.add_parser('udp_server', help="Start a UDP server")
    parser_udp_server.add_argument('host', type=str, help="Host address")
    parser_udp_server.add_argument('port', type=int, help="Port number")
    
    # UDP Client
    parser_udp_client = subparsers.add_parser('udp_client', help="Start a UDP client")
    parser_udp_client.add_argument('host', type=str, help="Host address")
    parser_udp_client.add_argument('port', type=int, help="Port number")
    parser_udp_client.add_argument('message', type=str, help="Message to send")
    
    # Chat Server
    parser_chat_server = subparsers.add_parser('chat_server', help="Start a chat server")
    parser_chat_server.add_argument('host', type=str, help="Host address")
    parser_chat_server.add_argument('port', type=int, help="Port number")
    
    # Chat Client
    parser_chat_client = subparsers.add_parser('chat_client', help="Start a chat client")
    parser_chat_client.add_argument('host', type=str, help="Host address")
    parser_chat_client.add_argument('port', type=int, help="Port number")
    
    # Add custom help description
    help_description = """
    Instructions for Running the Tool:

    1. Port Scanner:
       python socketprogram.py port_scanner <target_ip> <start_port> <end_port>
       Example: python socketprogram.py port_scanner 127.0.0.1 1 1024

    2. Banner Grabber:
       python socketprogram.py banner_grabber <target_ip> <target_port>
       Example: python socketprogram.py banner_grabber 127.0.0.1 80

    3. TCP Server:
       python socketprogram.py tcp_server <host> <port>
       Example: python socketprogram.py tcp_server 127.0.0.1 9999

    4. TCP Client:
       python socketprogram.py tcp_client <host> <port> <message>
       Example: python socketprogram.py tcp_client 127.0.0.1 9999 "Hi From Syed, TCP Server!"

    5. UDP Server:
       python socketprogram.py udp_server <host> <port>
       Example: python socketprogram.py udp_server 127.0.0.1 9999

    6. UDP Client:
       python socketprogram.py udp_client <host> <port> <message>
       Example: python socketprogram.py udp_client 127.0.0.1 9999 "Hi From Syed, UDP Server!"

    7. Chat Server:
       python socketprogram.py chat_server <host> <port>
       Example: python socketprogram.py chat_server 127.0.0.1 9999

    8. Chat Client:
       python socketprogram.py chat_client <host> <port>
       Example: python socketprogram.py chat_client 127.0.0.1 9999
    """
    
    parser.epilog = help_description
    
    args = parser.parse_args()
    
    if args.command == "port_scanner":
        open_ports = port_scanner(args.target_ip, args.start_port, args.end_port)
        print(f"Open ports on {args.target_ip}: {open_ports}")
    
    elif args.command == "banner_grabber":
        banner = banner_grabber(args.target_ip, args.target_port)
        print(f"Banner from {args.target_ip}:{args.target_port} - {banner}")
    
    elif args.command == "tcp_server":
        tcp_server(args.host, args.port)
    
    elif args.command == "tcp_client":
        tcp_client(args.host, args.port, args.message)
    
    elif args.command == "udp_server":
        udp_server(args.host, args.port)
    
    elif args.command == "udp_client":
        udp_client(args.host, args.port, args.message)
    
    elif args.command == "chat_server":
        chat_server(args.host, args.port)
    
    elif args.command == "chat_client":
        chat_client(args.host, args.port)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
