# RA 206341

# programinha pra printar matrizes de divisores
# tu não faz ideia de como eh belo ver uma matriz daquelas 100x100


def divisors(n):
    for i in range(1, int(n / 2) + 2):
        if n % i == 0:
            yield i
    yield n


n = int(input())
c = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i in divisors(j) or j in divisors(i):
            print("*", end="")
            c += 1
        else:
            print("-", end="")
    print()
print(c)
