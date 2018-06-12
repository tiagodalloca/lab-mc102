# O programa busca as melhores acoes dados os precos
n = int(input())
beast_wealth = 0
best_actions = []
p_matrix = [[float(input()) for v in range(n)]
            for _ in range(4)]  # price matrix


def calc_best_wealth(used, actions, start, end):
    global beast_wealth
    global best_actions

    if end >= n:
        curr_wealth = sum(map(lambda a: a[3], actions))
        if curr_wealth > beast_wealth:
            best_actions = []
            beast_wealth = curr_wealth
            best_actions.extend(actions)
    else:
        remaining = range(end + 1, n + 1)
        for i in set(range(4)) - used:
            chain_wealth = p_matrix[i][end] - p_matrix[i][start]
            if chain_wealth > 0:
                used.add(i)
                actions.append((i, start, end, chain_wealth))
                for d in remaining:
                    calc_best_wealth(used, actions, end, d)
                used.remove(i)
                actions.remove((i, start, end, chain_wealth))

        for d in remaining:
            calc_best_wealth(used, actions, end, d)


for day in range(1, n + 1):
    calc_best_wealth(set(), [], 0, day)

best_actions.sort()
for action in best_actions:
    val = (action[0] + 1, action[1] + 1, action[2] + 1, action[3])
    print("acao %d: compra %d, venda %d, lucro %.2f" % val)
print("Lucro: %.2f" % beast_wealth)
