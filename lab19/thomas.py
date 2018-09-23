# Thomas (Desnord)

# O objetivo desta tarefa é fazer um programa
# que use recursividade e que, dada a matriz 
# que descreve a hierarquia de uma empresa,
# encontre a cadeia hierárquica relativa a 
# um determinado funcionário.

#entrada:
# A primeira linha contém dois inteiros: n,
# o número de funcionários entre 3 e 30, e k,
# o identificador numérico do funcionário sobre
# o qual deseja-se conhecer a cadeira hierárquica. 
# A seguir tem-se n linhas que correspondem as 
# linhas da matriz que descrevem a hierarquia
# da empresa. 

#saída:
# Na saída devem ser impressos os números
# que identificam todos os funcionários 
# que estejam na cadeia hierárquica do 
# funcionário k, começando pelo próprio,
# e então imprimindo, em ordem crescente
# por identificador, os outros funcionários.

'''------------------------------------------'''

#lendo entradas
nk = input().split()
n = int(nk[0]) 
k = int(nk[1]) 

matriz = [] 

for i in range(n):
 linha = input().split()
 matriz.append(linha)

resultado = []
resultado.append(k)

#função recursiva para achar a cadeia hierarquica
def cadeiahier(mat, res):
 aux = res[:] 
 
 for i in range(len(mat[aux[len(aux)-1]])):
  if(int(mat[aux[len(aux)-1]][i]) == 1):
  	 res.append(i)
  	 res = cadeiahier(mat, res) 
  	 
 return res

#função para ordernar
def ckts(res):
    for w in range(len(res)-1, 0, -1):
        trocou = False
        for i in range(w, 0, -1):
            if (res[i] < res[i-1]):
                res[i], res[i-1] = res[i-1], res[i]
                trocou = True

        for i in range(w):
            if (res[i] > res[i+1]):
                res[i], res[i+1] = res[i+1], res[i]
                trocou = True
      
        if not trocou:
            return res
    
    return res

#gera a cadeia hierárquica 
resultado = cadeiahier(matriz,resultado) 

#arrumando a saída no formato exigido
resultado.remove(k) 

if(len(resultado) != 0):
 resultado = ckts(resultado) 
 resstr = ' '.join(map(str, resultado))
 print(str(k) +' '+ str(resstr))
else:
 print(k) 
