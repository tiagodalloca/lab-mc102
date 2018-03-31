'''O objetivo do programa é calcular o tamanho da circunferência,
nas unidades de medidas "estádios" e em "kilômetros", tendo como
dados a medida do raio e a medida do ângulo.'''

#Medida do raio
r = float(input())

#Medida do ângulo
a = float(input())

#Medida da circunferência em estádios
c = (360/a)*r

#Convertendo para kilômetros
ckm = (c*0.1764)

#Imprimindo os resultados
print("%.1f" %c)
print("%.1f" %ckm)
