#!/usr/bin/env python3

# Thomas (Desnord)

#objetivo: ler o arquivo com os registros das partidas e computar a tabela final do campeonato. 
# A tabela contem o nome do time, a pontuação, o número de vitórias, o saldo de gols e os gols prós. 
# A tabela é apresentada decrescentemente ordenada pela quantidade de pontos. 
# Em caso de empate no número de pontos, os critérios de desempate, em ordem de precedência, 
# são: número de vitórias, saldo de gols e gols prós.

#A 1ª linha da entrada é um inteiro n que indica a qtde de times no campeonato.
#As n linhas seguintes contém os nomes dos times.
#Após a sequência de times, temos uma sequência de partidas.
#partidas tem o formato: nomeDoTime1 GolsTime1 X NomeDoTime2 GolsDoTime2

#A saída é a tabela final do campeonato, 
#sendo que cada linha da tabela corresponde aos dados de um time.
#Uma linha tem o seguinte formato: NOME_TIME, PONTOS, NUMERO_DE_VITORIAS, SALDO_DE_GOLS, GOLS_PROS.


#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):

 jogoVet = [str(i) for i in jogo.split()]
 
 #time 1 venceu
 if(jogoVet[1] > jogoVet[3]):
  for i in range(len(tabela)):
      
     # altera os dados do time1
     if(tabela[i][0] == jogoVet[0]):
        tabela[i][1] = str(int(tabela[i][1]) + 3) #vitoria acrescenta 3 pontos
        tabela[i][2] = str(int(tabela[i][2]) + 1) #acrescenta 1 vitoria
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[3]) + int(jogoVet[1]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[1]))#modifica a qtde de gols pro
     
     #altera os dados do time2
     elif(tabela[i][0] == jogoVet[4]):
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[1]) + int(jogoVet[3]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[3]))#modifica a qtde de gols pro

 #time 2 venceu
 elif(jogoVet[1] < jogoVet[3]):
    for i in range(len(tabela)):
     
     #altera os dados do time2
     if(tabela[i][0] == jogoVet[4]):    
        tabela[i][1] = str(int(tabela[i][1]) + 3) #vitoria acrescenta 3 pontos
        tabela[i][2] = str(int(tabela[i][2]) + 1) #acrescenta 1 vitoria
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[1]) + int(jogoVet[3]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[3]))#modifica a qtde de gols pro

     #altera os dados do time1
     elif(tabela[i][0] == jogoVet[0]):
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[3]) + int(jogoVet[1]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[1]))#modifica a qtde de gols pro
 #empatou
 else:
    for i in range(len(tabela)):
    
     #altera os dados do time2
     if(tabela[i][0] == jogoVet[4]):
        tabela[i][1] = str(int(tabela[i][1]) + 1)#empate acrescenta 1 ponto
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[1]) + int(jogoVet[3]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[3]))#modifica a qtde de gols pro

     #altera os dados do time1
     elif(tabela[i][0] == jogoVet[0]):
        tabela[i][1] = str(int(tabela[i][1]) + 1)#empate acrescenta 1 ponto
        tabela[i][3] = str(int(tabela[i][3]) - int(jogoVet[3]) + int(jogoVet[1]))#calcula novo saldo de gols
        tabela[i][4] = str(int(tabela[i][4]) + int(jogoVet[1]))#modifica a qtde de gols pro

#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
  
  Time1Vet = time1
  Time2Vet = time2

  if(int(Time1Vet[1]) > int(Time2Vet[1])):#se o time1 tem mais pontos que o time2
   return 1
  elif(int(Time1Vet[1]) < int(Time2Vet[1])):
   return -1
  else:#se ha empate nos pontos
    if(int(Time1Vet[2]) > int(Time2Vet[2])):#se o time1 tem mais vitorias que o time2
     return 1
    elif(int(Time1Vet[2]) < int(Time2Vet[2])):
     return -1
    else:#se ha empate no numero de vitorias
     if(int(Time1Vet[3]) > int(Time2Vet[3])):#se o time1 tem saldo de gols melhor que o do time2
        return 1
     elif(int(Time1Vet[3]) < int(Time2Vet[3])):
        return -1
     else:#se ha empate no saldo de gols
        if(int(Time1Vet[4]) > int(Time2Vet[4])):#se o time1 tem mais gols pros do que o do time2
         return 1
        elif(int(Time1Vet[4]) < int(Time2Vet[4])):
         return -1
        else:
         return 0 #houve empate em todos os casos
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    
 FoiOrdenada = False #boolean que diz quando a tabela foi ordenada

 while(FoiOrdenada == False):    

  tabela2 = tabela[:] #a tabela auxiliar é uma copia da tabela

  for i in range(len(tabela)-1):#percorre a tabela
   if(comparaTimes(tabela[i],tabela[i+1]) == -1):#caso o time que esta na posicao a frente for maior que o time posicao

     #troca os dois times de posicao
     aux = tabela[i]
     tabela[i] = tabela[i+1]
     tabela[i+1] = aux

  #caso nao houver alteracoes na tabela, ela sera igual a tabela auxiliar
  #ou seja, a tabela ja está ordenada
  if(tabela2 == tabela):
    FoiOrdenada = True
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
 
 #imprime cada linha da tabela
 for i in range(len(tabela)):
   print(", ".join(map(str,tabela[i])))
 
