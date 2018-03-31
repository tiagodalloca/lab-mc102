'''O objetivo do programa é calcular quanto um passageiro deve pagar,
sabendo o pagamento inicial, descontos, taxa por distância, pontuação
do mesmo e pontos de origem e destino'''

#Valor inicial
vi = float(input())

#Coordenada x inicial
xi = float(input())

#Coordenada y inicial
yi = float(input())

#Coordenada x final
xf = float(input())

#Coordenada y final
yf = float(input())

#Tempo do percurso
t = float(input())

#Cupom
cd = float(input())

#Pontuação passageiro
pr = float(input())

#Distância
d = xf - xi + yf - yi

#Valor da corrida
VC = vi + d*t

#Valor do desconto
VD = max(cd, (VC*pr/100))

#Valor final
VF = VC - VD

#Imprimi o resultado
print("%.2f" % VF)
