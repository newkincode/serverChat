import socket
import threading
import json
import os

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
stop_thread = False

# from https://github.com/IamLucif3r/Chat-On/blob/main/client.py
def enter_server():
    os.system('cls||clear')
    ip = input("server ip : ")
    port = int(input("server port : "))
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to a host
    client.connect((ip, port))

def write():
    while True:
        if stop_thread:
            break
        # Getting Messages
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
# by nekwini
print("1. conect server")
print("2. add server list")
print("3. opnen server")
num = int(input("select: "))
print("\033[2J\033[H")

if num == 1:
    nickname = input("your name:")
    enter_server()
    write_thread = threading.Thread(target=write)
    write_thread.start()