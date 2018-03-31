# Rescebe os valores de entrada.
P1 = float(input())
P2 = float(input())
Ml = float(input())

# Calculo da media parcial.
Mp = (2 * P1 + 3 * P2) / 5.0

# Regras para aprovação.
if Ml < 5.0 or Mp < 5.0:
    M = min(Mp, 4.9)
else:
    M = (3 * Mp + 2 * Ml) / 5.0

if 5.0 > M >= 2.5:
    E = float(input())
    F = (M + E) / 2.0
else:
    F = M

# Imprime os resultados.
print("%.1f" % Mp)
print("%.1f" % M)
print("%.1f" % F)
