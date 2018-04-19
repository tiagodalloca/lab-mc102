# RA 206341

from functools import reduce
from math import ceil


data_base = {}

n = int(input())

for _ in range(n):
    (i, pca, pcf) = list(map(int, input().split()))
    if i in data_base:
        data_base[i].append(pcf / pca)
    else:
        data_base[i] = [pcf / pca]

for i in data_base:
    li = data_base[i]
    data_base[i] = reduce((lambda acc, x: acc + x), li) / len(li)

while(True):
    (i, pca) = list(map(int, input().split()))
    if i == 0 and pca == 0:
        break
    print(ceil(pca * data_base[i]))
