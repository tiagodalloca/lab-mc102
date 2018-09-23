# thomas (Desnord)

#!/usr/bin/env python3

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
    if(num in conj):
        return True
    else:
        return False

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
    for i in range(len(conj1)):
     if(not conj1[i] in conj2):
      return False

    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao
    if(not pertence(conj,num)):
     conj.append(num)

    return

def subtracao(conj, num):
    # Implementar a funcao
    if(pertence(conj,num)):
     conj.remove(num)

    return

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
    # Implementar a funcao e trocar o valor de retorno

    uni = list(conj1)

    for i in range(len(conj2)):
     if(not conj2[i] in uni):
      uni.append(int(conj2[i]))

    return uni

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno

    its = []

    for i in range(len(conj1)):
     if(conj1[i] in conj2):
      its.append(int(conj1[i]))

    return its

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    difc = []

    for i in range(len(conj1)):
        if(not conj1[i] in conj2):
         difc.append(int(conj1[i]))

    return difc

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    return (uniao(diferenca(conj1,conj2),diferenca(conj2,conj1)))
