# Thomas (Desnord)

# entrada: 2 arquivos, a imagem à ser feita a convolucao e um arquivo
# do tipo texto, com a matriz de convolucao e o divisor d

# saida: convolucao da imagem da entrada, no formato pgm

# objetivo: fazer a convolucao de uma imagem

import sys

s1 = str(sys.argv[1])
s2 = str(sys.argv[2])

arq1 = open(s1, 'r')
arq2 = open(s2, 'r')

''' lendo a imagem '''
I = []
cont = 0
dl = 0
dc = 0

pgm = arq1.readlines()
for l in pgm :
    if(cont == 0):
        cont = 1
    elif(cont == 1):
        aux = l.split()
        dc = aux[0]
        dl = aux[1]
        cont = 2
    elif(cont == 2):
        cont = 3
    else:
        I.append(list(l.split()))

arq1.close()
'''--------------'''

''' lendo M e D '''
M = []
D = 0
cont = 0

txt = arq2.readlines()
for l in txt :
    if(cont == 0):
     D = int(l)
     cont = 1
    else:
     M.append(list(l.split()))

arq2.close()
'''--------------'''

''' fazendo a convolucao da img '''
I2 = []
linha = []

for i in  range(int(dl)):
    for j in  range(int(dc)):
        linha.append(I[i][j])
    I2.append(linha)
    linha = []

for i in range(1,len(I)-1):
    for j in  range(1,len(I[i])-1):
          p = (int(M[0][0]) * int(I[i-1][j-1]))
          p+= (int(M[0][1]) * int(I[i-1][j]))
          p+= (int(M[0][2]) * int(I[i-1][j+1]))

          p+= (int(M[1][0]) * int(I[i][j-1]))
          p+= (int(M[1][1]) * int(I[i][j]))
          p+= (int(M[1][2]) * int(I[i][j+1]))

          p+= (int(M[2][0]) * int(I[i+1][j-1]))
          p+= (int(M[2][1]) * int(I[i+1][j]))
          p+= (int(M[2][2]) * int(I[i+1][j+1]))
          p = int(p/D)

          if(p < 0):
              p = 0
          if(p > 255):
              p = 255

          I2[i][j] = p


'''-----------------------------'''

''' dando a saída em um arquivo pgm '''
l2 = dc+' '+dl

print('P2')
print(l2)
print('255')

for i in range(int(dl)):
    atual = str(' '.join(map(str, I2[i])))
    print(atual+'  ')

'''
arq3 = open('resultado.pgm', 'w')
arq3.write('P2\n')
arq3.write(l2+'\n')
arq3.write('255\n')

for i in range(int(dl)):
    atual = str(' '.join(map(str, I2[i])))
    arq3.write(atual+'  '+'\n')

arq3.close()'''
'''---------------------------------'''
