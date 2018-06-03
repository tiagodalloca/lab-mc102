# O seu objetivo e fazer um programa que calcula quanto um passageiro tera que pagar para uma determinada viagem,
# ou seja, o valor final VF. O programa recebe o valor do pagamento inicial, os pontos de origem e destino do
# passageiro, a taxa por cada unidade de distancia percorrida, o valor do cupom e a pontuacao do passageiro. O programa
# deve entao calcular o valor a ser pago pelo passageiro que e dado pela formula  VF = VC - VD

vi, xi, yi, xf, yf, t, cd, pr = [float(input()) for x in range(8)]

vc = vi + ((xf - xi) + (yf - yi)) * t
VF = vc - max(cd, (vc * pr / 100.0))

print('%.2f' % VF)
