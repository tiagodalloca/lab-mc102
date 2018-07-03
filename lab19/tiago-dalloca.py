# RA 206341

# programa para achar hierarquias
# yay


def acha_subordinados(k, m):
    l = []
    for (i, f) in enumerate(m[k]):
        if f != 0:
            l += acha_subordinados(i, m)
    l.sort()
    return [k] + l


(n, k) = list(map(int, input().split()))

m = [list(map(int, input().split())) for _ in range(n)]

print(" ".join(map(str, acha_subordinados(k, m))))
