# RA 206341


def ler_tabuleiro(h, w):
    return [list(input()) for i in range(h)]


def fazer_ataque(tab, l, c):
    if tab[l][c] == "@":
        tab[l][c] = "-"
        acessar_loc(tab, l + 1, c)
        acessar_loc(tab, l - 1, c)
        acessar_loc(tab, l, c + 1)
        acessar_loc(tab, l, c - 1)


def acessar_loc(tab, y, x):
    if len(tab) > y and y >= 0:
        if len(tab[y]) > x and x >= 0:
            fazer_ataque(tab, y, x)


def print_tab(tab):
    for i in tab:
        print("".join(i))


(h, w) = list(map(int, input().split('x')))
tab1 = ler_tabuleiro(h, w)
tab2 = ler_tabuleiro(h, w)

vez_do_1 = True

while True:
    (l, c) = list(map(int, input().split(',')))
    if vez_do_1:
        fazer_ataque(tab2, l - 1, c - 1)
        print("Ataque em (%d,%d) do jogador 1" % (l, c))
        print_tab(tab2)
        if all("@" not in x for x in tab2):
            break
    else:
        fazer_ataque(tab1, l - 1, c - 1)
        all("@" not in x for x in tab1)
        print("Ataque em (%d,%d) do jogador 2" % (l, c))
        print_tab(tab1)
        if all("@" not in x for x in tab1):
            break
    vez_do_1 = not vez_do_1
