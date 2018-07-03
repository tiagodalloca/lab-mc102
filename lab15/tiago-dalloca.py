#!/usr/bin/env python3

# RA 206341


from functools import reduce


# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#


def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno
    return num in conj

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#


def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    return reduce((lambda acc, x: x in conj2 and acc), conj1, True)

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#


def adicao(conj, num):
    if len(conj) < 20 and num not in conj:
        return conj.append(num)
    return conj


def subtracao(conj, num):
    if len(conj) > 0 and num in conj:
        return conj.remove(num)
    return conj

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#


def uniao(conj1, conj2):
    return list(set(conj1 + conj2))


def intersecao(conj1, conj2):
    return [x for x in conj1 if x in conj1 and x in conj2]


def diferenca(conj1, conj2):
    return [x for x in conj1 if x not in conj2]


def uniao_disjunta(conj1, conj2):
    return [x for x in conj1 + conj2
            if (x in conj1 and x not in conj2) or
            (x in conj2 and x not in conj1)]
