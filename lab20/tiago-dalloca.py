#!/usr/bin/env python3

import copy

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku

boxes = [
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9]
]


def n_of_box(i, j):
    x = boxes[i][j]
    return [[n, m] for n in range(9) for m in range(9) if boxes[n][m] == x]

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario


def resolve(resposta):
    # print_sudoku(resposta)
    for i in range(9):
        for j in range(9):
            if resposta[i][j] == 0:
                ok = [n for n in range(1, 10)
                      if (n not in [resposta[l][j] for l in range(9)])
                      and n not in resposta[i]
                      and n not in [resposta[t][v]
                                    for (t, v) in n_of_box(i, j)]]
                for k in ok:
                    resposta[i][j] = k
                    nu = copy.deepcopy(resposta)
                    if (resolve(nu)):
                        for l in range(9):
                            resposta[l] = nu[l]
                        return True
                return False
    return True
