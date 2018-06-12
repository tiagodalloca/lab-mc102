#!/usr/bin/env python3

# RA 206341


def letscallitawin(j1, j2, g1, g2, tabela):
    for i, (j, p, v, gs, gp) in enumerate(tabela):
        if j == j1:
            tabela[i] = [j, p + 3, v + 1, gs + g1 - g2, gp + g1]
        elif j == j2:
            tabela[i] = [j, p, v, gs - g1 + g2, gp + g2]


def atualizaTabela(tabela, jogo):
    jogo = jogo.split(" ")
    j1 = jogo[0]
    j2 = jogo[-1]
    g1 = int(jogo[1])
    g2 = int(jogo[-2])
    if g1 > g2:
        letscallitawin(j1, j2, g1, g2, tabela)
    elif g1 < g2:
        letscallitawin(j2, j1, g2, g1, tabela)
    else:
        for i, (j, p, v, gs, gp) in enumerate(tabela):
            if j == j1 or j == j2:
                tabela[i][-1] += g1
                tabela[i][1] += 1


def ordenaTabela(tabela):
    list.sort(tabela, key=lambda x: x[1: len(x)], reverse=True)


def imprimeTabela(tabela):
    for x in tabela:
        print(", ".join(map(str, x)))
