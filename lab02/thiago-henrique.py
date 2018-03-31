'''O objetivo do programa é calcular quanto um passageiro deve pagar,
sabendo o pagamento inicial, descontos, taxa por distância, pontuação
do mesmo e pontos de origem e destino'''

#Valores de entrada
vi = float(input())
xi = float(input())
yi = float(input())
xf = float(input())
yf = float(input())
t = float(input())
cd = float(input())
pr = float(input())

#Distância
d = xf - xi + yf - yi

#Valor da corrida
VC = vi + d*t

#Valor do desconto
VD = max(cd, (VC*pr/100))

#Valor final
VF = VC - VD

#Resultado
print("%.2f" % VF)
