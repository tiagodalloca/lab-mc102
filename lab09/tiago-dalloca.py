# RA 206341

# o role aqui eh loco e nois vai estorar essa bolsa
# recebe valores de ações e cospe o caminho para a riqueza

import itertools


def valid_comb(comb, values):
    current_company = -1
    sold_companies = []
    profit = 0
    for i, day in enumerate(comb):
        if day[1] != -1:
            if current_company == -1 or current_company != day[1]:
                return (False, -1)
            if day[1] == current_company:
                current_company = -1
                sold_companies.append(day[1])
                profit += values[day[1]][i]
        if current_company == -1:
            if day[0] != -1:
                if day[0] not in sold_companies:
                    current_company = day[0]
                    profit -= values[day[0]][i]
                else:
                    return (False, -1)
        elif day[0] != -1:
            return (False, -1)
    return (True, profit)


# valores das ações para cada dia
# são 4 empresas, dentro vão ter valores para cada dia 0 <= x <= d
values = [[], [], [], []]

d = int(input())

for j in range(4):
    for i in range(d):
        values[j].append(float(input()))

perms = list(itertools.permutations(range(-1, 4), 2))
perms.append((-1, -1))
# combinations = itertools.product(perms, repeat=d) melhorado
combinations = [[]]
for p_perm in [perms] * d:
    combinations = (x + [y] for x in combinations for y in p_perm
                    if len(x) == 0 or valid_comb(x, values)[0])

# capitalismo HUAHUAHUAHUA
max_profit = 0
max_profit_comb = [[-1, -1]] * d
for comb in combinations:
    (_, p) = valid_comb(comb, values)
    if p > max_profit:
        max_profit = p
        max_profit_comb = comb

c = [-1] * 4
v = c.copy()

for i, day in enumerate(max_profit_comb):
    if day[0] != -1:
        c[day[0]] = i + 1
    if day[1] != -1:
        v[day[1]] = i + 1

for i in range(4):
    if c[i] != -1 and v[i] != -1:
        print("acao %d: compra %d, venda %d, lucro %.2f" %
              (i + 1, c[i], v[i],
               (values[i][v[i] - 1] - values[i][c[i] - 1])))

print("Lucro: %.2f" % max_profit)
