# Thomas (Desnord)

# O objetivo deste laboratório é, dada a configuração inicial da população,
# simular o estado da população durante alguns dias utilizando as regras
# de interação humano/zumbi definidas no enunciado.

# A 1ª linha da entrada é composta por dois inteiros, m e n,
# representando respectivamente o número de linhas e colunas da matriz.
# A 2ª linha contém um inteiro i,
# que representa o nº de dias que desejamos simular o estado da população.
# À seguir temos cada uma das m linhas da matriz.

# a saída reporta o estado da população para cada um dos i dias transcorridos.
# (incluindo o dia inicial)


dimensao = input()

dvetor = [int(ty) for ty in dimensao.split()]

m = dvetor[0] #numero de linhas
n = dvetor[1] #numero de colunas
i = int(input()) #dias para simular o estado da populacao

matriz = [] # status atual da populacao
matrizDiaSeguinte = [] # status da populacao para o dia seguinte
linha = [] # linha da matriz 
leitura = [] # entrada das informacoes da populacao

'''---------------------------------------------------------------------'''
# le os dados da matriz
for k in range(0,m+2):
   if(k!=0 and k!=m+1):
    leitura = [int(v) for v in input().split()]
   for h in range(0,n+2):
    if(k == 0 or k == m+1 or h == 0 or h == n+1):        
      linha.append(0)
    else:
      linha.append(int(leitura[h-1]))
 
   matriz.append(linha[:])
   matrizDiaSeguinte.append(linha[:])
   linha = []

'''---------------------------------------------------------------------'''
printar = []
# imprime o estado inicial da populacao
print("iteracao 0")
for qw in range(1,m+1):
  printar = []
  for zw in range(1,n+1):
      printar.append(int(matriz[qw][zw]))

  if(len(printar) != 0):
   print("".join(map(str,printar)))
  
'''---------------------------------------------------------------------'''
for ww in range(i):#para cada dia percorrido
  for zz in range(1,m+1):#para cada linha
    for kk in range(1,n+1):#para cada coluna

        if(matriz[zz][kk] == 0):# x é vazio

           humano = 0
           
           # verifica a qtde de humanos ao redor de x
           if(matriz[zz][kk+1] == 1):
                humano += 1
           if(matriz[zz][kk-1] == 1):
                humano += 1
           if(matriz[zz+1][kk] == 1):
                humano += 1
           if(matriz[zz-1][kk] == 1):
                humano += 1
           if(matriz[zz+1][kk+1] == 1):
                humano += 1
           if(matriz[zz-1][kk+1] == 1):
                humano += 1
           if(matriz[zz+1][kk-1] == 1):
                humano += 1
           if(matriz[zz-1][kk-1] == 1):
                humano += 1

           if(humano == 2):#dois humanos ao redor de x
              matrizDiaSeguinte[zz][kk]= 1#nasce um novo humano em x
              
        elif(matriz[zz][kk] == 1):# x é humano
         if(matriz[zz][kk+1] == 2 or matriz[zz][kk-1] == 2 or matriz[zz+1][kk] == 2 or matriz[zz-1][kk] == 2 or matriz[zz+1][kk+1] == 2 or matriz[zz-1][kk-1] == 2 or matriz[zz+1][kk-1] == 2 or matriz[zz-1][kk+1] == 2):#um ou mais zumbis ao redor de x
            matrizDiaSeguinte[zz][kk] = 2#o humano em x é infectado

        elif(matriz[zz][kk] == 2):# x é zumbi
           humano = 0
           
           # verifica a qtde de humanos ao redor de x
           if(matriz[zz][kk+1] == 1):
                humano += 1
           if(matriz[zz][kk-1] == 1):
                humano += 1
           if(matriz[zz+1][kk] == 1):
                humano += 1
           if(matriz[zz-1][kk] == 1):
                humano += 1
           if(matriz[zz+1][kk+1] == 1):
                humano += 1
           if(matriz[zz-1][kk+1] == 1):
                humano += 1
           if(matriz[zz+1][kk-1] == 1):
                humano += 1
           if(matriz[zz-1][kk-1] == 1):
                humano += 1

           if(humano == 0):#nenhum humano ao redor de x
            matrizDiaSeguinte[zz][kk] = 0#o zumbi morre de fome

           elif(humano >= 2):#dois ou mais humanos ao redor de x
                   matrizDiaSeguinte[zz][kk] = 0#zumbi é morto pelos humanos

  print("iteracao %d" %(ww+1))
  #passando para o dia seguinte dia, atualiza o estado da populacao
  #e imprime o estado da populacao
  for pp in range(1,m+1):
    printar = []
    for uu in range(1,n+1):
        matriz[pp][uu] = int(matrizDiaSeguinte[pp][uu])
        printar.append(int(matriz[pp][uu]))
    
    if(len(printar)):
     print("".join(map(str,printar)))
