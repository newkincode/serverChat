import socket

def opne():
    print("server")
    ip = "127.0.0.1"
    port = int(input("port: "))
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip, port))
    server_socket.listen()
    while True:
        client_socket, addr = server_socket.accept()
        print('conect: ', addr)
        data = client_socket.recv(1024)
        if not data:
            break
        print('received: ', addr, data.decode())
        client_socket.sendall(data)
opne()