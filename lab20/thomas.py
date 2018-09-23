#!/usr/bin/env python3

'''---------------------------------------------------------------------------------------'''
# Thomas (Desnord)

# entrada: A entrada do programa será de 9x9 dígitos de 0 a 9, 
# onde 0 representa as posições com valores indefinidos que devem ser resolvidas.

# saida: A saída do programa é composta da grade antes e depois da solução, 
# com separadores - e | para linhas e colunas, respectivamente.

# objetivo: resolver jogos de sudoku, de forma recursiva

'''---------------------------------------------------------------------------------------'''

# Funcao: print_sudoku
# Essa funcao ja esta implementada no arquivo lab20_main.py
# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku


# O aluno pode criar outras funcoes que ache necessario
def resolve_recursao(mat,l,c):
 
    #acha o proximo espaco vazio
    if(mat[l][c] != 0):
        while (mat[l][c] != 0):
            if(c < 8):
                c += 1
            elif(c == 8):
                l += 1
                c = 0
            
            if(l > 8):
                return mat

    #cria string com a linha da posicao atual
    linhastr = "".join(map(str,mat[l]))

    #cria string com a coluna da posicao atual
    colunastr = ""
    for k in range(len(mat)):
        colunastr += str(mat[k][c])

    #cria string com o bloco da posicao atual
    blocostr = ""
    if(l == 0 or l == 1 or l == 2):
        if(c == 0 or c == 1 or c ==2):#bloco 1
            blocostr =  str(mat[0][0])+str(mat[0][1])+str(mat[0][2])
            blocostr += str(mat[1][0])+str(mat[1][1])+str(mat[1][2])
            blocostr += str(mat[2][0])+str(mat[2][1])+str(mat[2][2])
        elif(c == 3 or c == 4 or c == 5):#bloco 2
            blocostr =  str(mat[0][3])+str(mat[0][4])+str(mat[0][5])
            blocostr += str(mat[1][3])+str(mat[1][4])+str(mat[1][5])
            blocostr += str(mat[2][3])+str(mat[2][4])+str(mat[2][5])
        else:#bloco 3
            blocostr =  str(mat[0][6])+str(mat[0][7])+str(mat[0][8])
            blocostr += str(mat[1][6])+str(mat[1][7])+str(mat[1][8])
            blocostr += str(mat[2][6])+str(mat[2][7])+str(mat[2][8])
    elif(l == 3 or l == 4 or l == 5):
        if(c == 0 or c == 1 or c ==2):#bloco 4
            blocostr =  str(mat[3][0])+str(mat[3][1])+str(mat[3][2])
            blocostr += str(mat[4][0])+str(mat[4][1])+str(mat[4][2])
            blocostr += str(mat[5][0])+str(mat[5][1])+str(mat[5][2])
        elif(c == 3 or c == 4 or c == 5):#bloco 5
            blocostr =  str(mat[3][3])+str(mat[3][4])+str(mat[3][5])
            blocostr += str(mat[4][3])+str(mat[4][4])+str(mat[4][5])
            blocostr += str(mat[5][3])+str(mat[5][4])+str(mat[5][5])            
        else:#bloco 6
            blocostr =  str(mat[3][6])+str(mat[3][7])+str(mat[3][8])
            blocostr += str(mat[4][6])+str(mat[4][7])+str(mat[4][8])
            blocostr += str(mat[5][6])+str(mat[5][7])+str(mat[5][8])  
    else:
        if(c == 0 or c == 1 or c ==2):#bloco 7
            blocostr =  str(mat[6][0])+str(mat[6][1])+str(mat[6][2])
            blocostr += str(mat[7][0])+str(mat[7][1])+str(mat[7][2])
            blocostr += str(mat[8][0])+str(mat[8][1])+str(mat[8][2])    
        elif(c == 3 or c == 4 or c == 5):#bloco 8
            blocostr =  str(mat[6][3])+str(mat[6][4])+str(mat[6][5])
            blocostr += str(mat[7][3])+str(mat[7][4])+str(mat[7][5])
            blocostr += str(mat[8][3])+str(mat[8][4])+str(mat[8][5]) 
        else:#bloco 9
            blocostr =  str(mat[6][6])+str(mat[6][7])+str(mat[6][8])
            blocostr += str(mat[7][6])+str(mat[7][7])+str(mat[7][8])
            blocostr += str(mat[8][6])+str(mat[8][7])+str(mat[8][8]) 

    #realiza o backtracking
    for i in range(1,10):
        
        if(linhastr.__contains__(str(i)) == False and colunastr.__contains__(str(i)) == False and blocostr.__contains__(str(i)) == False ):

            mat[l][c] = i
            print_sudoku(mat)
            mat = resolve_recursao(mat,l,c)

            tabstr = ""
            for j in range(len(mat)):
                tabstr += "".join(map(str,mat[j]))
            
            if(tabstr.__contains__("0")):
                mat[l][c] = 0
            else:
                break

    return mat
                        

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(tab):
    # Implementar a funcao e trocar o valor de retorno

    tab = resolve_recursao(tab,0,0)                   
                            
    strJogo = ""
    for k in range(9):
        strJogo += "".join(map(str,tab[k]))

    if(strJogo.__contains__("0")):
        return False
    else:
        print_sudoku(tab)
        return True    