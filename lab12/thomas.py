#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome: Thomas (Desnord)

# objetivo: Simular uma versão simplificada de Tetris, onde os únicos blocos possíveis são retângulos

# A entrada é composta apenas dos blocos que deverão ser inseridos no tabuleiro.
# A primeira linha da entrada contém o número de blocos n. 
# À seguir temos n linhas contendo 5 inteiros nessa ordem: largura, altura, posicao horizontal inicial,
# deslocamento horizontal do bloco(neg. desloca pra esquerda, e pos. desloca pra direita), binario de rotacao (0 nao rotaciona e 1 rotaciona)

# A saída será o estado do tabuleiro após a inserção de cada bloco válido no seguinte formato:
# A primeira linha conterá bloco k, onde k é o índice do bloco inserido (começando em 0),
# a próxima linha contém os pontos acumulados até aquele momento, 
# e à seguir será impresso o próprio tabuleiro.

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10


#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda) 
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario 
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
    # Implementar a funcao e trocar o valor de retorno
     
    # se o bloco deve ser rotacionado
    if(rot == 1):
     #inverte altura com largura
     aux = l 
     l = a
     a = aux  

    #desloca o x
    x = x + desl

    #impede que o bloco extrapole o tabuleiro pelos lados
    if(x < 0):
     x = 0
    elif(x+l > 9):
     x = 10 - l

    return l, a, x 

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro 
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):
    # Implementar a funcao e trocar o valor de retorno
    ynovo = -1
    achou = 0

    for i in range(len(mat)-1,-1,-1):#percorre o tabuleiro
     for j in range(x,x+l): #nos pontos horizontais que o bloco ocuparia

      if(mat[i][j] == 1): #achou uma posicao que o bloco n pode ocupar
       ynovo = i+1  #o bloco deve ocupar a partir da linha de cima
       achou = 1
       break
     if(achou == 1):
      break
     else:
      if(i == 0):#quando o bloco deve ficar no inicio do tabuleiro
       ynovo = 0
       break
      
    
    return ynovo
       


# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
    
    if(y+a <= 10):#se o não bloco extrapola o tabuleiro
     return 1
    else:
     return 0
# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro 
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posições ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):
    # Implementar a funcao
    
    #dentro do espaco que o bloco ocupará
    for i in range(y,y+a):  
     for j in range(x,x+l):        
      mat[i][j] = 1 #um pedaco do bloco preenche a posicao

    return 

# Funcoes: atualiza_matriz
# 
#    mat: matriz do tabuleiro 
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):
    # Implementar a funcao e trocar o valor de retorno
    nlPreenchidas = 0

    #acha o numero de linha a serem removidas
    for k in range(len(mat)):
     if(mat[k].__contains__(0) == False):
      nlPreenchidas += 1

    cont = 0
    while(cont < nlPreenchidas):#enquanto todas as linhas que devem ser removidas, nao forem removidas
     cont += 1
     for i in range(len(mat)):#percorrendo cada linha do tabuleiro
        
      if(mat[i].__contains__(0) == False):# se a linha esta totalmente preenchida
       
        if(i == 9): #caso a linha preenchida seja o topo do tabuleiro de tetris
          for j in range(10):
           mat[9][j] = 0 #simplesmente zera todas as colunas do topo
          
        else: #caso a linha preenchida nao seja o topo

          for w in range(i,10):#da linha i, ate a ultima linha
           for q in range(10):#cada coluna
            if(w != 9):
             mat[w][q] = int(mat[w+1][q])#desce o elemento acima, 1 posicao
             mat[w+1][q] = 0#o elemento de cima eh zerado
            else:
             mat[w][q] = 0
          
    
    return nlPreenchidas
