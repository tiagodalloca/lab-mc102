# thomas (Desnord)

#objetivo: verificar em uma matriz quando um indice for divisor do outro e
# quantas vezes isso ocorre

#entrada: dimensao da matriz
#saida: linhas da matriz e o valor do contador

x = int(input());#le a dimensao da matriz
m = list(range(x));#cria uma vetor com a dimensao especificada
cont = 0;#inicia o contador

for i in range (x):
    for j in range (x):
        if((i+1)%(j+1) == 0 or (j+1)%(i+1) == 0):#caso um indice for divisor do outro
            m[j]= '*';
            cont += 1;
        else:
            m[j]= '-';
    print("".join(map(str,m)));#escreve todo os valores do vetor/linha,
                               #antes de passar para a proxima

print(cont);#escreve o valor do contador, que representa a quantidade de
            #vezes em que os indices eram divisiveis
