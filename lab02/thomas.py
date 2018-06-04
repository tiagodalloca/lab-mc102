# thomas (Desnord)

# objetivo: calcular o valor final da corrida que um passageiro deve pagar

# entrada:
# (as quais sao usadas para calcular o valor da corrida)
#   valor inicial da corrida,cordenadas da origem e do destino do passageiro,
#   taxa cobrada por unidade de distancia;
# (as quais sao usadas para calcular o desconto)
#   cupom de desconto e pontuacao do rebelde

# saida: valor final, que o passageiro devera pagar

vi = int(input()); # entrada para o valor inicial
xi = int(input()); # entrada para a cordenada x inicial
yi = int(input()); # entrada para a cordenada y inicial
xf = int(input()); # entrada para a cordenada x final
yf = int(input()); # entrada para a cordenada y final
t = int(input()); # entrada para a taxa cobrada por unidade de distancia
cd = int(input()); # entrada para o cupom de desconto
pr = int(input()); # entrada para a pontuacao do rebelbe

d = (xf - xi) + (yf - yi); # calcula a distancia
vc = vi + d*t; # calcula o valor da corrida
vd = max(cd, (vc * pr/100)); # verifica o melhor desconto

vf = vc - vd; # calcula o valor final da corrida,considerando o desconto

print("%.2f" % vf) # saida do valor final da corrida
