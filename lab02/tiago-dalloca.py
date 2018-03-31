# RA 206341

# extraído do texto

# VF = VC - VD

# VC = vi + d * t

# d = (xf - xi) + (yf - yi)

# VD = MAX(cd, (VC * pr/100))


def read_int():
    return int(input())


vi, xi, yi, xf, yf, t, cd, pr = \
    list(map((lambda x: read_int()), range(8)))

d = (xf - xi) + (yf - yi)
VC = vi + d * t
VD = max(cd, (VC * pr / 100))
VF = VC - VD

print("%.2f" % VF)
