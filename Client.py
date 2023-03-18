import keyboard
import Server

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
runing = True
select = 1
selectCount = 0
def run():
    global select,selectCount
    while True:
        print(BACKGROUND_BLUE+"                                    ServerChat 0.1a                                    ")
        print(RESET)
        if select == 1:
            print("|----------------------------------|")
            print("|                                  |")
            print(BACKGROUND_WHITE+"|          conect server           |"+RESET)
            print("|          add server list         |")
            print("|            opne server           |")
            print("|                                  |")
            print("|                                  |")
            print("|                                  |")
            print("|----------------------------------|")
        if select == 2:
            print("|----------------------------------|")
            print("|                                  |")
            print("|          conect server           |")
            print(BACKGROUND_WHITE+"|          add server list         |"+RESET)
            print("|            opne server           |")
            print("|                                  |")
            print("|                                  |")
            print("|                                  |")
            print("|----------------------------------|")
        if select == 3:
            print("|----------------------------------|")
            print("|                                  |")
            print("|          conect server           |")
            print("|          add server list         |")
            print(BACKGROUND_WHITE+"|            opne server           |"+RESET)
            print("|                                  |")
            print("|                                  |")
            print("|                                  |")
            print("|----------------------------------|")

        if keyboard.KEY_UP:
            if keyboard.is_pressed("DOWN"):
                if selectCount == 50:
                    select += 1
                    selectCount=0
                if select >= 3:
                    select = 3
                    selectCount=0
                selectCount+=1
            if keyboard.is_pressed("UP"):
                if selectCount == 50:
                    select -= 1
                    selectCount=0
                if select <= 1:
                    select = 1
                    selectCount=0
                selectCount+=1
            if keyboard.is_pressed("ENTER"):
                break
                

        print(select)

        print("\033[2J\033[H")
run()