# thomas (desnord)

# o programa tem o objetivo de calcular a circuferencia de um planeta
# tendo por entradas:
# d: distancia entre as duas cidades
# a: angulo medido
# tendo por saida:
# ce: circuferencia em estadios
# ckm: circuferencia em kilometros

#digitar a distancia e depois o angulo:

d = float(input()); #distância entre 2 pontos
a = float(input()); #graus do angulo

Ce = 360*d/a; #calcula a circuferencia em estadios
Ckm = 360*d*0.1764/a; #calcula a circuferencia em km

#escreve os valores obtidos para cada unidade
print("%.1f" %Ce);
print("%.1f" %Ckm);
