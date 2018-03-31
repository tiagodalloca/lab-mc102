# RA 206341

# DESCRIÇÃO

# Escreva um programa que calcule a circunferência C de um determinado
# planeta, com base na observação do ângulo A, entre duas localidades C1 e
# C2, e na distância D, em estádios, entre elas.

# Suponha que as localidades estejam no mesmo meridiano de um planeta
# esférico. O seu programa deverá imprimir a circunferência do planeta em
# estádios e em quilômetros.

# ENTRADA

# A entrada do programa será composta da distância D, em estádios, e do
# ângulo A, em graus, respectivamente, um número em cada linha.

# SAÍDA

# A saída mostra a circunferência Ce, em estádios, e Ckm, em quilômetros,
# do planeta seguindo o cálculo feito por Eratóstenes para a Terra com uma
# casa decimal de precisão.


def read_float():
    return float(input())


# converte e para km
def e_to_km(e):
    return 0.1764 * e


# printa floats com 1 digito depois da vírgula
def print_1f(f):
    print("%.1f" % f)


D = read_float()
A = read_float()

# 360/A = o número de vezes que a distância D
# ocorre no planeta
E = D * (360 / A)

print_1f(E)
print_1f(e_to_km(E))
