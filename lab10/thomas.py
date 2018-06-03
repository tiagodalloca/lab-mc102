''' thomas (Desnord)'''

#   Entrada: consiste de um texto de no máximo 1000 caracteres, e uma série de identificadores de operações 
#   e seus respectivos parâmetros

''' Saida: deverá ser impresso o texto lido como entrada e, para cada operação realizada sobre o texto, deve ser 
    impresso o texto com a modificação decorrente da operação e o programa deve ler outra operação.Quando
    o programa ler o operador Q, que representa a operação de sair, o programa deve encerrar a execução.'''

#   objetivo: como programador da Aliança Rebelde, você deve criar um programa que, dado um texto,
#   um identificador de uma operação e seus parâmetros, realiza as modificações necessárias no texto.

'''----------------------------------------------------------------------------------------------------------------'''

texto = str(input())#le o texto
opcao = ""#le a primeira opcao
print(texto)#mostra o texto inicial

textoMatriz = [str(i) for i in texto.split()]#matriz do texto, utilizada para as operacoes

#enquanto nao for digitada a opcao de sair
while(opcao != 'Q'):
 #opcao de deletar (delete)    
 if(opcao == 'D'):
  p_del = str(input()).upper()#le a palavra que tera suas ocorrencias apagada

  for i in range (len(textoMatriz)):#procura todas as ocorrencias da palavra no texto

   if(textoMatriz[i].upper() == p_del or textoMatriz[i].upper() == (p_del+",") or
      textoMatriz[i].upper() == (p_del+":") or textoMatriz[i].upper() == (p_del+"!") or
      textoMatriz[i].upper() == (p_del+"?") or textoMatriz[i].upper() == (p_del+".")):#quando achar uma ocorrencia

      textoMatriz[i] = ""#apaga a palavra
  
  #remove os espacos extras no novo texto e o escreve na tela
  texto = ' '.join(map(str, textoMatriz))
  texto = texto.replace("  "," ")
  texto = texto.strip(' ')
  textoMatriz = [str(i) for i in texto.split()]
  texto = ' '.join(map(str, textoMatriz))
  print(texto)
 #opcao de inverter (inverse)
 elif(opcao == 'I'):
   p_inv = str(input()).upper()#le a palavra que tera suas ocorrencias invertidas

   for i in range (len(textoMatriz)):#procura todas as ocorrencias da palavra no texto
    
    #para cada caso, inverte a palavra corretamente
    if(textoMatriz[i].upper() == p_inv):
      textoMatriz[i] = textoMatriz[i][::-1]    

    if(textoMatriz[i].upper() == (p_inv+",")):
      textoMatriz[i] = textoMatriz[i].replace(",","")
      textoMatriz[i] = textoMatriz[i][::-1] 
      textoMatriz[i] = textoMatriz + ","

    if(textoMatriz[i].upper() == (p_inv+":")): 
      textoMatriz[i] = textoMatriz[i].replace(":","")
      textoMatriz[i] = textoMatriz[i][::-1] 
      textoMatriz[i] = textoMatriz[i] + ":"

    if(textoMatriz[i].upper() == (p_inv+"!")):
      textoMatriz[i] = textoMatriz[i].replace("!","")
      textoMatriz[i] = textoMatriz[i][::-1] 
      textoMatriz[i] = textoMatriz[i] + "!"

    if(textoMatriz[i].upper() == (p_inv+"?")): 
      textoMatriz[i] = textoMatriz[i].replace("?","")
      textoMatriz[i] = textoMatriz[i][::-1] 
      textoMatriz[i] = textoMatriz[i] + "?"

    if(textoMatriz[i].upper() == (p_inv+".")):
      textoMatriz[i] = textoMatriz[i].replace(".","")
      textoMatriz[i] = textoMatriz[i][::-1] 
      textoMatriz[i] = textoMatriz[i] + "."

    texto = ' '.join(map(str, textoMatriz))
    textoMatriz = [str(i) for i in texto.split()]
   #escreve o novo texto
   print(texto)
 #opcao de substituir (replace)
 elif(opcao == 'R'):
   p_old = str(input()).upper()#le a palavra que tera suas ocorrencias substituidas
   p_new = str(input())#le a palavra que sera colocada no lugar de cada ocorrencia da anterior

   for i in range (len(textoMatriz)):#procura todas as ocorrencias da palavra antiga no texto

    # substitui corretamente, em cada caso da palavra 
    if(textoMatriz[i].upper() == p_old):
      textoMatriz[i] = p_new  

    if(textoMatriz[i].upper() == (p_old+",")):
      textoMatriz[i] = textoMatriz[i].replace(",","")
      textoMatriz[i] = p_new 
      textoMatriz[i] = textoMatriz + ","

    if(textoMatriz[i].upper() == (p_old+":")): 
      textoMatriz[i] = textoMatriz[i].replace(":","")
      textoMatriz[i] = p_new 
      textoMatriz[i] = textoMatriz[i] + ":"

    if(textoMatriz[i].upper() == (p_old+"!")):
      textoMatriz[i] = textoMatriz[i].replace("!","")
      textoMatriz[i] = p_new 
      textoMatriz[i] = textoMatriz[i] + "!"

    if(textoMatriz[i].upper() == (p_old+"?")): 
      textoMatriz[i] = textoMatriz[i].replace("?","")
      textoMatriz[i] = p_new 
      textoMatriz[i] = textoMatriz[i] + "?"

    if(textoMatriz[i].upper() == (p_old+".")):
      textoMatriz[i] = textoMatriz[i].replace(".","")
      textoMatriz[i] = p_new 
      textoMatriz[i] = textoMatriz[i] + "."

   #remove os espacos extras do novo texto e o escreve na tela
   texto = ' '.join(map(str, textoMatriz))
   texto = texto.replace("  "," ")
   texto = texto.strip(' ')
   textoMatriz = [str(i) for i in texto.split()]
   print(texto)

 opcao = input()
'''----------------------------------------------------------------------------------------------------------------'''