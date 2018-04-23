# Gabriel Teston 

# Recebendo numero de dias
n = int(input())
# Definindo historico de acoes
hist = []
for emp in range(4):
    linha = []
    for day in range(n):
        linha.append(float(input()))
    hist.append(linha)
    
# Definindo as funcoes necessarias
def is_intercet(actions):
    """ Retorna se ha interseccao entre os dias de compra e venda entre as empresas. """
    for x, action in enumerate(actions):
        for y, action2 in enumerate(actions):
            if x != y:
                if action[0] in range(action2[0], action2[1]) and action != [0, 0]:
                    return True

def is_valid(actions):
    """ Retorna se as combinacoes de compra e venda da acoes respeitam ordem cronologica. """
    for action in actions:
        if action != [0, 0]:
            if action[0] >= action[1]:
                return False
    return True

# Definindo todas as combinacoes de compra e venda
profits = []
for ic1, dc1 in enumerate(hist[0]):
    for iv1, dv1 in enumerate(hist[0]):
        for ic2, dc2 in enumerate(hist[1]):
            for iv2, dv2 in enumerate(hist[1]):
                for ic3, dc3 in enumerate(hist[2]):
                    for iv3, dv3 in enumerate(hist[2]):
                        for ic4, dc4 in enumerate(hist[3]):
                            for iv4, dv4 in enumerate(hist[3]):
                                actions = [[ic1, iv1], [ic2, iv2], [ic3, iv3], [ic4, iv4]]
                                if not is_valid(actions) or is_intercet(actions):
                                    pass
                                else:
                                    profits.append([(dv1-dc1)+(dv2-dc2)+(dv3-dc3)+(dv4-dc4), actions])
# Definindo maior lucro possivel
if len(profits) > 0:
    max_profit = max(profits)
    for i, ops in enumerate(max_profit[1]):
        if ops != [0, 0]:
            print("acao %d: compra %d, venda %d, lucro %.2f" % 
                  (i + 1, ops[0] + 1, ops[1] + 1, hist[i][ops[1]] - hist[i][ops[0]]))
else:
    max_profit = 0
print("Lucro: %.2f" % max_profit[0])