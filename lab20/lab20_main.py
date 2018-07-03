#!/usr/bin/env python3

import sys
import time

colors_list = dict()
colors_list["reset"] = '\x1b[0m'
colors_list["sep"] = '\x1b[0;34;44m'
colors_list["sep2"] = '\x1b[0;36;46m'
colors_list["input"] = '\x1b[0;37;40m'
colors_list["player"] = '\x1b[0;30;47m'
colors_list["wrong"] = '\x1b[0;37;41m'
colors_list["change"] = '\x1b[0;30;43m'

TTY = None
# Verifica e habilita cores no terminal


def enable_colors():
    global TTY
    if TTY is not None:
        return TTY
    TTY = sys.platform in ["linux", "darwin"]
    TTY = TTY and hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    TTY = TTY and hasattr(sys.stdin, 'isatty') and sys.stdin.isatty()
    return TTY

# Limpa a tela do terminal


def clearScreen():
    if enable_colors():
        print("\x1b[2J\x1b[1;1H", end="")


def gotoScreen(x, y):
    if enable_colors():
        print("\x1b[{0:d};{1:d}H".format(x, y), end="")


# Configura o terminal para enviar os caracteres sem enter e sem
# monstra-los na tela
tty_settings = None


def enable_getch():
    global tty_settings
    if enable_colors():
        import termios
        fd = sys.stdin.fileno()
        tty_settings = termios.tcgetattr(fd)
        try:
            tty_settings[3] &= ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, tty_settings)
        finally:
            pass

# Desativa configuracao especial do terminal


def disable_getch():
    global tty_settings
    if tty_settings is not None:
        import termios
        fd = sys.stdin.fileno()
        tty_settings[3] |= termios.ICANON | termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, tty_settings)

# Imprime cores e formatacao de texto


def printc(color):
    if enable_colors():
        sys.stdout.write(color)


resposta = [[-1 for x in range(9)] for y in range(9)]
original = [[-2 for x in range(9)] for y in range(9)]
ultima = [[-1 for x in range(9)] for y in range(9)]


def print_pos(resposta, x, y):
    global original
    global ultima
    global colors_list

    if enable_colors():
        if ultima[x][y] != resposta[x][y]:
            printc(colors_list["change"])
            ultima[x][y] = resposta[x][y]
            print("", resposta[x][y], end=" ")
            return
        elif original[x][y] > 0:
            if original[x][y] != resposta[x][y]:
                printc(colors_list["wrong"])
            else:
                printc(colors_list["input"])
        else:
            printc(colors_list["player"])
    if resposta[x][y] > 0:
        print("", resposta[x][y], end=" ")
    else:
        sys.stdout.write("   ")


def print_hline(color2):
    global colors_list
    printc(colors_list["sep"])
    sys.stdout.write("-")
    printc(color2)
    sys.stdout.write("-----------")
    printc(colors_list["sep"])
    sys.stdout.write("-")
    printc(color2)
    sys.stdout.write("-----------")
    printc(colors_list["sep"])
    sys.stdout.write("-")
    printc(color2)
    sys.stdout.write("-----------")
    printc(colors_list["sep"])
    sys.stdout.write("-\n")


def _print_sudoku(resposta):
    global colors_list

    clearScreen()
    for i in range(0, 9):
        if i % 3 == 0:
            print_hline(colors_list["sep"])
        else:
            print_hline(colors_list["sep2"])

        for j in range(0, 9):
            if j % 3 == 0:
                printc(colors_list["sep"])
            else:
                printc(colors_list["sep2"])

            sys.stdout.write('|')
            print_pos(resposta, i, j)

        printc(colors_list["sep"])
        sys.stdout.write('|')
        printc(colors_list["reset"])
        sys.stdout.write('\n')

    print_hline(colors_list["sep"])
    printc(colors_list["reset"])
    sys.stdout.flush()


def print_sudoku(resposta):
    if enable_colors():
        _print_sudoku(resposta)
        time.sleep(0.001)


# Importa funcoes implementadas pelo aluno
import sys
import os
sys.path.insert(0, os.getcwd())

if __name__ == '__main__':

    enable_getch()  # Configura terminal
    clearScreen()

    print_sudoku(resposta)
    for i in range(0, 9):
        for j in range(0, 9):
            c = sys.stdin.read(1)[0]
            while True:
                try:
                    original[i][j] = int(c)
                    resposta[i][j] = original[i][j]
                    break
                except ValueError:
                    c = sys.stdin.read(1)[0]
                    continue
            if enable_colors():
                _print_sudoku(resposta)
    _print_sudoku(resposta)

    from lab20 import resolve
    if resolve(resposta):
        _print_sudoku(resposta)
    else:
        print("Nao foi encontrada uma solucao.")

    disable_getch()  # Volta o terminal as configuracoes originais
