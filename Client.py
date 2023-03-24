import keyboard
import socket

RESET = "\u001B[0m"
FONT_BLACK = "\u001B[30m"
FONT_RED = "\u001B[31m"
FONT_GREEN = "\u001B[32m"
FONT_YELLOW = "\u001B[33m"
FONT_BLUE = "\u001B[34m"
FONT_PURPLE = "\u001B[35m"
FONT_CYAN = "\u001B[36m"
FONT_WHITE = "\u001B[37m"
BACKGROUND_BLACK = "\u001B[40m"
BACKGROUND_RED = "\u001B[41m"
BACKGROUND_GREEN = "\u001B[42m"
BACKGROUND_YELLOW = "\u001B[43m"
BACKGROUND_BLUE = "\u001B[44m"
BACKGROUND_PURPLE = "\u001B[45m"
BACKGROUND_CYAN = "\u001B[46m"
BACKGROUND_WHITE = "\u001B[47m"

print("1. conect server")
print("2. add server list")
print("3. opnen server")
num = int(input("select: "))
print("\033[2J\033[H")
if num == 1:
    user = input("name: ")
    ip = input("ip: ")
    port = int(input("port: "))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    while True:
        msg = input("msg: ")
        if msg == "/exit":
            break
        print("\033[2J\033[H")
        client_socket.sendall(f'{user} : {msg}'.encode())
        data = client_socket.recv(1024)
        print(repr(data.decode()))
    client_socket.close()