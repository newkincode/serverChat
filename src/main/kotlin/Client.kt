
import java.io.IOException


const val RESET = "\u001B[0m"
const val FONT_BLACK = "\u001B[30m"
const val FONT_RED = "\u001B[31m"
const val FONT_GREEN = "\u001B[32m"
const val FONT_YELLOW = "\u001B[33m"
const val FONT_BLUE = "\u001B[34m"
const val FONT_PURPLE = "\u001B[35m"
const val FONT_CYAN = "\u001B[36m"
const val FONT_WHITE = "\u001B[37m"
const val BACKGROUND_BLACK = "\u001B[40m"
const val BACKGROUND_RED = "\u001B[41m"
const val BACKGROUND_GREEN = "\u001B[42m"
const val BACKGROUND_YELLOW = "\u001B[43m"
const val BACKGROUND_BLUE = "\u001B[44m"
const val BACKGROUND_PURPLE = "\u001B[45m"
const val BACKGROUND_CYAN = "\u001B[46m"
const val BACKGROUND_WHITE = "\u001B[47m"

fun gotoxy(x: Int, y: Int){
    for(i in 1..y) {
        print("\n")
    }
    for(i in 1..x){
        print(" ")
    }
}

fun main(args: Array<String>) {
    while (true) {
        print(BACKGROUND_RED) // 배경색 설정
        gotoxy(100, 0)
        println("serverChat v0.1a")
        print(BACKGROUND_BLACK) // 배경색 설정
        println("|---------------------------------|")
        println("|           conect server         |")
        println("|                                 |")
        println("|                                 |")
        println("|                                 |")
        println("|                                 |")
        println("|                                 |")
        println("|---------------------------------|")
        
    }
}