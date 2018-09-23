# thomas (Desnord)

# objetivo: realizar operações com uma lista de RAs
# imprimir,ordenar crescente,ordenar decrescente,
# realizar busca binaria, remover valor, adicionar valor.

#A entrada consiste de: uma lista com n inteiros (RA de cada aluno)
#e uma lista de operações a serem realizadas finalizada pelo caractere s.

#Deverá ser impressa a lista como lida na entrada e,
#para cada operação 'p' realizada deve ser impressa a lista no estado atual, dadas as operações realizadas anteriormente.
#Quando o programa ler o operador s, que representa a operação de sair, o programa deve encerrar a execução.

'''--------------------------------------------------------------------------'''
def buscaBinariaCrescente (lista ,valor):
 inicio= 0
 fim = len(lista) - 1
 a = ''

 while(inicio <= fim):#enquanto a busca n for finalizada
  meio = ( inicio+fim )//2 #meio da sublista
  a+= str(meio)+" "

  if (lista[meio] == valor): #se o valor for encontrado
   print(a)
   return meio #retorna a posicao que o valor foi encontrado

  elif (lista[meio] > valor): #novo final da sublista
   fim = meio-1

  else:#novo inicio da sublista
   inicio = meio+1

 print(a)
 return -1

def buscaBinariaDecrescente (lista ,valor):
 inicio= 0
 fim = len(lista) - 1
 a = ''

 while(inicio <= fim):#enquanto a busca n for finalizada
  meio = ( inicio+fim )//2 #meio da sublista
  a+= str(meio)+" "

  if (lista[meio] == valor): #se o valor for encontrado
   print(a)
   return meio #retorna a posicao que o valor foi encontrado

  elif(lista[meio] < valor):#novo final da sublista
   fim = meio-1

  else:#novo inicio da sublista
   inicio = meio+1

 print(a)
 return -1

valores = input()
alunos = [int(a) for a in valores.split()]

opcao = 'a'
ordenacao = 0 #0 - ordenada, 1 ordenada cres e -1 ordenada decresc

while(opcao != 's'):

    x = input().split()
    opcao = x[0]

    if(opcao == 'p'):
      if(len(alunos) != 0):
          
       '''for i in alunos:
        if(i != alunos[len(alunos)-1]):
         print(int(i), end=" ")
        else:
         print(int(i), end="\n") ''' 

       printstring = " ".join(map(str,alunos[:]))
       print(printstring+ " ")

    elif(opcao == 'c'):

        FoiOrdenada = False #boolean que diz quando a lista foi ordenada
        ordenacao = 1 

        while(FoiOrdenada == False):

         alunos2 = alunos[:] #a tabela auxiliar é uma copia da tabela

         for i in range(len(alunos)-1):#percorre a lista
          if(alunos[i] > alunos[i+1]):

            #troca os dois times de posicao
            aux = alunos[i]
            alunos[i] = alunos[i+1]
            alunos[i+1] = aux

         #caso nao houver alteracoes na lista, ela sera igual a lista auxiliar
         #ou seja, a lista ja está ordenada
         if(alunos2 == alunos):
           FoiOrdenada = True

    elif(opcao == 'd'):

        FoiOrdenada = False #boolean que diz quando a lista foi ordenada
        ordenacao = -1

        while(FoiOrdenada == False):

         alunos2 = alunos[:] #a tabela auxiliar é uma copia da tabela

         for i in range(len(alunos)-1):#percorre a lista
          if(alunos[i] < alunos[i+1]):

            #troca os dois times de posicao
            aux = alunos[i]
            alunos[i] = alunos[i+1]
            alunos[i+1] = aux

         #caso nao houver alteracoes na lista, ela sera igual a lista auxiliar
         #ou seja, a lista ja está ordenada
         if(alunos2 == alunos):
           FoiOrdenada = True

    elif(opcao == 'b'):
     valor = int(x[1])

     if(ordenacao != 0):#se a lista esta ordenada de alguma forma

       if(ordenacao == 1):#se esta ordenada crescente
        buscou = buscaBinariaCrescente(alunos,valor)

        if(buscou != -1):
         print("%d esta na posicao: %d"%(valor, buscou))
        else:
         print("%d nao esta na lista!"%(valor))

       else:#se esta ordenada decrescente
        buscou = buscaBinariaDecrescente(alunos,valor)

        if(buscou != -1):
         print("%d esta na posicao: %d"%(valor, buscou))
        else:
         print("%d nao esta na lista!"%(valor))

     else:
      print("Vetor nao ordenado!")

    elif(opcao == 'i'):
     valor = int(x[1])

     if(len(alunos) == 150):
      print("Limite de vagas excedido!")
     else:
       if(valor in alunos):
        print("Aluno ja matriculado na turma!")
       else:
        alunos.append(valor)

        if(ordenacao == 1):
             FoiOrdenada = False #boolean que diz quando a lista foi ordenada

             while(FoiOrdenada == False):

              alunos2 = alunos[:] #a tabela auxiliar é uma copia da tabela

              for i in range(len(alunos)-1):#percorre a lista
                if(alunos[i] > alunos[i+1]):

                 #troca os dois times de posicao
                 aux = alunos[i]
                 alunos[i] = alunos[i+1]
                 alunos[i+1] = aux

              #caso nao houver alteracoes na lista, ela sera igual a lista auxiliar
              #ou seja, a lista ja está ordenada
              if(alunos2 == alunos):
               FoiOrdenada = True

        elif(ordenacao == -1):
             FoiOrdenada = False #boolean que diz quando a lista foi ordenada

             while(FoiOrdenada == False):

              alunos2 = alunos[:] #a tabela auxiliar é uma copia da tabela

              for i in range(len(alunos)-1):#percorre a lista
                if(alunos[i] < alunos[i+1]):

                 #troca os dois times de posicao
                 aux = alunos[i]
                 alunos[i] = alunos[i+1]
                 alunos[i+1] = aux

              #caso nao houver alteracoes na lista, ela sera igual a lista auxiliar
              #ou seja, a lista ja está ordenada
              if(alunos2 == alunos):
               FoiOrdenada = True

    elif(opcao == 'r'):
     valor = int(x[1])

     if(len(alunos) == 0):#caso n exista alunos na lista
      print("Nao ha alunos cadastrados na turma!")
     else:
      if(valor in alunos):#se o valor existe na lista
        alunos.remove(valor)
      else:
        print("Aluno nao matriculado na turma!")
