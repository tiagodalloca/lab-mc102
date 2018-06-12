# thomas (Desnord)

# entrada: numero de evolucoes de monstros que serao registradas,
# registros de evolucoes e consultas de dados

# saida: o pcf (poder de combate final) dos monstros, de acordo
# com os dados consultados

# objetivo: calcular o possivel poder de combate de monstros
# de um jogo, apos evoluirem

import math

n = int(input())  # le o numero de evolucoes que serao registradas

bd = []  # banco de dados de monstros
ints = []  # vetor usado para leitura de dados
m = float(0)  # multiplicador de evolucao
b = 0

# registra as evolucoes de monstros
while(len(ints) != 2):
    linha = input()
    ints = [int(i) for i in linha.split()]
    bd.append(ints)

# le as consultas de dados,
# faz os calculos necessarios e retorna o pcf ao usuario
while(ints[0] != 0 and ints[1] != 0):
    if(b != 0):
        linha = input()
        ints = [int(i) for i in linha.split()]

    b = 1
    aux = 1
    aux2 = 0

    # percorre todo o bd e axa o valor do multiplicador medio
    # para o monstro atual
    for i in range(0, len(bd) - 1):
        if(bd[i][0] == ints[0]):
            m += bd[i][2] / bd[i][1]
            if(aux2 != 0):
                aux += 1
            aux2 = 1

    m /= aux

    if(ints[1] != 0):
        print("%.0f" % math.ceil(ints[1] * m))  # imprime o valor do pcf
        #(arredondado para cima)
        m = float(0)
