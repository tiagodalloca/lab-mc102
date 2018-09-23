# Thomas (Desnord)

#objetivo:
# simular uma partida de batalha naval

#entrada:
# A primeira linha determina o tamanho LxC
# do tabuleiro, que representa o número de
# linhas e colunas, respectivamente
# Em seguida são apresentados os tabuleiros
# iniciais do jogador 1 e do jogador 2.
# Após a entrada correspondente aos tabuleiros 
# temos outras linhas indicando as jogadas
# de ataques. 

#saída:
# Para cada jogada, deve ser impresso um texto
# que identifica o jogador que fez o ataque e
# a coordenada do ataque.
# Em seguida deve ser impresso o tabuleiro do 
# jogador atacado.
# Caso um navio tenha sido destruído 
# são impressos os caracteres -, 
# correspondentes a água, em seu lugar.

'''------------------------------------------'''

#lendo entradas
lc = input().split("x")
l = int(lc[0])
c = int(lc[1])

tab1 = []
tab2 = []

for i in range(l):
 linha = input()
 linhavet = []
 for k in range(len(linha)):
     linhavet.append(linha[k])

 tab1.append(linhavet)

for i in range(l):
 linha = input()
 linhavet = []
 for k in range(len(linha)):
     linhavet.append(linha[k])

 tab2.append(linhavet)

#executando ataques e dando saídas
tab1str = ' '.join(map(str, tab1))
tab2str = ' '.join(map(str, tab2))
jatual = '1'

#funcao recursiva para afundar um navio
def derrubanavio(mat,x,y):
    mat[x][y] = '-'

    try:
        if(mat[x+1][y] == '@'):
            derrubanavio(mat,x+1,y)
    except:
        pass

    try:
        if(mat[x-1][y] == '@' and x != 0):
            derrubanavio(mat,x-1,y)
    except:
        pass

    try:
        if(mat[x][y-1] == '@' and y != 0):
            derrubanavio(mat,x,y-1)
    except:
        pass
    
    try:
        if(mat[x][y+1] == '@'):
            derrubanavio(mat,x,y+1)
    except:
        pass



while(tab1str.__contains__('@') and tab2str.__contains__('@')):

    ataque = input().split(',')
    print('Ataque em (' + ataque[0]+ ',' + ataque[1] + ') do jogador' +' '+jatual)
    
    if(jatual == '1'):
        if(tab2[int(ataque[0])-1][int(ataque[1])-1] == '@'):
            derrubanavio(tab2, int(ataque[0])-1, int(ataque[1])-1)

        jatual = '2'
        for i in range(l):
            print(''.join(map(str, tab2[i])))
        
    else:
        if(tab1[int(ataque[0])-1][int(ataque[1])-1] == '@'):
            derrubanavio(tab1, int(ataque[0])-1, int(ataque[1])-1)
            
        jatual = '1'
        for i in range(l):
            print(''.join(map(str, tab1[i])))

    tab1str = ''.join(map(str, tab1))
    tab2str = ''.join(map(str, tab2))
