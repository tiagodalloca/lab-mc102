# RA 206341

# Programa que calcula média de MC102


def read_float():
    return float(input())


P1 = read_float()
P2 = read_float()
ML = read_float()

# regras da média

MP = (2*P1 + 3*P2)/5

if MP < 5 or ML < 5:
    M = min(MP, 4.9)

else:
    M = (3*MP + 2*ML)/5

if 2.5 <= M and M < 5:
    E = read_float()
    F = (M + E)/2

else:
    F = M

# print do resultado

print("%.1f" % MP)
print("%.1f" % M)
print("%.1f" % F)
