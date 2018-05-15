from math import ceil

n = int(input())
db = [input().split() for i in range(n)]

avg_map = lambda e: (e[0], float(e[2]) / float(e[1]))
db = [v for v in map(avg_map, db)]

esp = {e[0]: 0 for e in db}
for k in esp.keys():
    mults = [v[1] for v in filter(lambda e: e[0] == k, db)]
    esp[k] = sum(mults) / len(mults)


def read_line():
    line = input()
    while line != '0 0':
        yield line.split()
        line = input()


result = [ceil(esp[q[0]] * float(q[1])) for q in read_line()]
print(*result, sep='\n')
