# thomas (desnord)

# objetivo: avaliar os valores diários dos blocos de ações de
# 4 empresas e decidir qual é o melhor dia para comprar e
# vender as ações de cada empresa

# entrada: um valor inteiro d representando a quantidade de
# dias no período analisado,d valores reais para cada uma
# das 4 empresas avaliadas,representando os valores do
# bloco de ações da empresa em cada dia,do 1 até o dia d.

# saida: imprimir para cada empresa as informacoes:
# acao N: compra DC, venda DV, lucro LC

'''------------------------------------------------------------------------------------------------------------'''
#objeto compra
class Compra:
  def __init__(self,empresa,dtCompra,dtVenda,lucro):
    self.empresa = empresa
    self.dtCompra = dtCompra
    self.dtVenda = dtVenda
    self.lucro = lucro

  def setEmpresa(self, empresa):
    self.empresa = empresa

  def setDtCompra(self, dtCompra):
    self.dtCompra = dtCompra

  def setDtVenda(self, dtVenda):
    self.dtVenda = dtVenda

  def setLucro(self, lucro):
    self.lucro = lucro

  def getEmpresa(self):
    return self.empresa

  def getDtCompra(self):
    return self.dtCompra

  def getDtVenda(self):
    return self.dtVenda

  def getLucro(self):
    return self.lucro
'''------------------------------------------------------------------------------------------------------------'''
d = int(input())#le o intervalo de dias considerado
bd = []#banco de informacoes
linha = []

# preenche o banco de informacoes de acoes
for i in range (4):
 for j in range (d):
  linha.append(float(input()))

 bd.append(linha)
 linha = []
'''------------------------------------------------------------------------------------------------------------'''
#acha todas as possibidades de compra para todas as empresas, desde que o lucro seja positivo
possCompra = []
aux = []
a = Compra(-1,-1,-1,-1)

for i in range (0,4):
 for j in range (0,d-1):
  for k in range (j+1,d):
   if(bd[i][k]-bd[i][j] > 0):
    a = Compra(i+1,j+1,k+1,bd[i][k]-bd[i][j])

   if(a.getEmpresa() != -1):
    aux.append(a)
    a = Compra(-1,-1,-1,-1)

e1 = []
e2 = []
e3 = []
e4 = []

for i in range(len(aux)):
 if(aux[i].getEmpresa() == 1):
  e1.append(Compra(aux[i].getEmpresa(),aux[i].getDtCompra(),aux[i].getDtVenda(),aux[i].getLucro()))
 elif(aux[i].getEmpresa() == 2):
  e2.append(Compra(aux[i].getEmpresa(),aux[i].getDtCompra(),aux[i].getDtVenda(),aux[i].getLucro()))
 elif(aux[i].getEmpresa() == 3):
  e3.append(Compra(aux[i].getEmpresa(),aux[i].getDtCompra(),aux[i].getDtVenda(),aux[i].getLucro()))
 elif(aux[i].getEmpresa() == 4):
  e4.append(Compra(aux[i].getEmpresa(),aux[i].getDtCompra(),aux[i].getDtVenda(),aux[i].getLucro()))

if(len(e1) != 0):
 possCompra.append(e1[:])
if(len(e2) != 0):
 possCompra.append(e2[:])
if(len(e3) != 0):
 possCompra.append(e3[:])
if(len(e4) != 0):
 possCompra.append(e4[:])
'''------------------------------------------------------------------------------------------------------------'''
possNegocio = [] #todos os negocios possiveis de serem feitos
aux = [] #negocio atual
lucro_total = 0.00
melhor = 0 #index do melhor negocio possivel

# se existem possibilidades de compra
if(len(possCompra) != 0):
 # encontra todas as possibilidades de negocios possiveis
 for i in range(len(possCompra)):
  for j in range(len(possCompra[i])):
    aux = []
    aux.append(Compra(possCompra[i][j].getEmpresa(),possCompra[i][j].getDtCompra(),possCompra[i][j].getDtVenda(),possCompra[i][j].getLucro()))#adiciona compra ao negocio
    possNegocio.append(aux[:])#guarda o negocio atual

    for k in range(len(possCompra)):
     for w in range (len(possCompra[k])):
      #se a compra verificada ainda nao existe no negocio e se ela nao da conflito de data com outra compra ja inserida no negocio
      if(possCompra[i][j].getEmpresa() != possCompra[k][w].getEmpresa() and (possCompra[i][j].getDtVenda() <= possCompra[k][w].getDtCompra() or possCompra[k][w].getDtVenda() <= possCompra[i][j].getDtCompra())):
         aux.append(Compra(possCompra[k][w].getEmpresa(),possCompra[k][w].getDtCompra(),possCompra[k][w].getDtVenda(),possCompra[k][w].getLucro()))#adiciona compra ao negocio
         possNegocio.append(aux[:])#guarda o negocio atual

         for e in range(len(possCompra)):
           for r in range(len(possCompra[e])):
             #se a compra verificada ainda nao existe no negocio e se ela nao da conflito de data com outra compra ja inserida no negocio
             if(possCompra[e][r].getEmpresa() != possCompra[k][w].getEmpresa() and possCompra[e][r].getEmpresa() != possCompra[i][j].getEmpresa() and
               (possCompra[e][r].getDtVenda() <= possCompra[k][w].getDtCompra() or possCompra[k][w].getDtVenda() <= possCompra[e][r].getDtCompra()) and
               (possCompra[e][r].getDtVenda() <= possCompra[i][j].getDtCompra() or possCompra[i][j].getDtVenda() <= possCompra[e][r].getDtCompra())):
              aux.append(Compra(possCompra[e][r].getEmpresa(),possCompra[e][r].getDtCompra(),possCompra[e][r].getDtVenda(),possCompra[e][r].getLucro()))#adiciona compra ao negocio
              possNegocio.append(aux[:])#guarda o negocio atual

              for t in range(len(possCompra)):
                for y in range(len(possCompra[t])):
                    #se a compra verificada ainda nao existe no negocio e se ela nao da conflito de data com outra compra ja inserida no negocio
                    if(possCompra[t][y].getEmpresa() != possCompra[e][r].getEmpresa() and possCompra[t][y].getEmpresa() != possCompra[k][w].getEmpresa() and
                       possCompra[t][y].getEmpresa() != possCompra[i][j].getEmpresa() and
                       (possCompra[t][y].getDtVenda() <= possCompra[k][w].getDtCompra() or possCompra[k][w].getDtVenda() <= possCompra[t][y].getDtCompra()) and
                       (possCompra[t][y].getDtVenda() <= possCompra[i][j].getDtCompra() or possCompra[i][j].getDtVenda() <= possCompra[t][y].getDtCompra()) and
                       (possCompra[e][r].getDtVenda() <= possCompra[t][y].getDtCompra() or possCompra[t][y].getDtVenda() <= possCompra[e][r].getDtCompra())):
                      aux.append(Compra(possCompra[t][y].getEmpresa(),possCompra[t][y].getDtCompra(),possCompra[t][y].getDtVenda(),possCompra[t][y].getLucro()))#adiciona compra ao negocio
                      possNegocio.append(aux[:])#guarda o negocio atual
                      aux = aux[:-1]#remove a ultima compra do negocio, para testar a proxima possibilidade
              aux = aux[:-1]#remove a ultima compra do negocio, para testar a proxima possibilidade
         aux = aux[:-1]#remove a ultima compra do negocio, para testar a proxima possibilidade

 #apos encontrar todos os negocios, verifica qual deles é o melhor (maior lucro)
 for i in range(len(possNegocio)):
  lucro_atual = 0.00
  for j in range(len(possNegocio[i])):
   lucro_atual += possNegocio[i][j].getLucro()
   if(lucro_atual > lucro_total):
     lucro_total = lucro_atual
     melhor = i

 #escreve as informacoes das melhores compras de um negocio
 for i in range(len(possNegocio[melhor])):
   print("acao %d: compra %d, venda %d, lucro %.2f" % (possNegocio[melhor][i].getEmpresa(), possNegocio[melhor][i].getDtCompra(), possNegocio[melhor][i].getDtVenda(), possNegocio[melhor][i].getLucro()))

 #imprime o lucro total do melhor um negocio
 print("Lucro: %.2f" % (lucro_total))

else:
 print("Lucro: 0.00")
