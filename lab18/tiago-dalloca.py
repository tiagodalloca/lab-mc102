# RA 206341

import sys


class AcessoAPosicaoInvalida(Exception):
    pass


def p(m, d, i, x, y):
    if x == 0 or y == 0 or y == len(i) - 1 or x == len(i[0]) - 1:
        return i[y][x]
    c = (
        m[0][0] * i[y - 1][x - 1] +
        m[0][1] * i[y - 1][x] +
        m[0][2] * i[y - 1][x + 1] +
        m[1][0] * i[y][x - 1] +
        m[1][1] * i[y][x] +
        m[1][2] * i[y][x + 1] +
        m[2][0] * i[y + 1][x - 1] +
        m[2][1] * i[y + 1][x] +
        m[2][2] * i[y + 1][x + 1]
    ) // d

    if c < 0:
        c = 0
    if c > 255:
        c = 255
    return c


def ler(fname):
    with open(fname) as f:
        content = f.readlines()
    return [x.strip() for x in content]


itexto = ler(sys.argv[1])
(m, n) = list(map(int, itexto[1].split()))
del itexto[0]
del itexto[0]
del itexto[0]
imagem = [list(map(int, l.split())) for l in itexto]

mtexto = ler(sys.argv[2])
d = int(mtexto[0])
del mtexto[0]
matriz = [list(map(int, l.split())) for l in mtexto]

print("P2")
print(m, n)
print(255)

for y in range(n):
    linha = []
    for x in range(m):
        linha.append(p(matriz, d, imagem, x, y))
    print(" ".join(map(str, linha)), " ", end="")
    print()
