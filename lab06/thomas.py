# thomas (Desnord)

# objetivo: simular uma luta entre Ryu e Ken e determinar quem ganhou a luta,
# considerando o multiplicador de danos

# entrada: sequencia de numeros, indicando o dano recebido por cada personagem
# (numero negativo = ryu levou dano; numero positivo: ken levou dano)

# saida: apos um lutador receber uma sequencia de golpes, exibe a vida dele
# antes de receber o combo, subtraindo o dano do combo.
# Ao final dos dois rounds, exibe o resultado da luta (empate ou
# tal lutador venceu)

r = 2000  # vida do ryu
k = 2000  # vida do ken

combo = 0  # dano sequenciado
x = 0  # dano lido

vr = 0  # rounds ganhos do ryu
vk = 0  # rounds ganhos do ken

#-------------------------------------------------------------------#
# round1
while(r > 0 and k > 0):  # enquanto alguem nao fica sem vida
    x = int(input())  # lê um dano
    testarnum = 0  # variavel usada para testar a naturaza do dano lido
    ehperfeito = 0  # var p/ informar se o num eh perfeito ou nao

    # testar se ele eh perfeito
    if(abs(x) != 1):
        for i in range(1, abs(x)):
            if(x % i == 0):
                testarnum += i

    # se o num eh perfeito, o multiplicador de danos por 3 eh usado
    if(testarnum == abs(x)):
        x *= 3
        ehperfeito = 1

    # se o numero nao eh perfeito, ele ainda pode ser triangular
    if(ehperfeito == 0):
        testarnum = 0
        cont = 1
        while(testarnum <= abs(x)):  # testa se o num eh triangular
            testarnum += cont
            cont += 1
            if(testarnum == abs(x)):  # caso for triangular
                x *= 2  # atribui multiplicador de danos por 2
                break

    if(combo < 0 and x > 0):  # ryu levou dano
        print("Ryu: %d" % r + " - %d" % abs(combo) + " = %d" % (r + combo))
        r += combo
        combo = x
    elif(combo > 0 and x < 0):  # ken levou dano
        print("Ken: %d" % k + " - %d" % combo + " = %d" % (k - combo))
        k -= combo
        combo = x
    elif(combo >= 0 and x > 0 and (k - combo) > 0):  # continuando combo
        combo += x
    elif(combo <= 0 and x < 0 and (r + combo) > 0):  # continuando combo
        combo += x

    # verifica se o combo ja é capaz de derrotar um lutador
    #(impede chutar cachorro morto)
    if((r + combo) <= 0):
        print("Ryu: %d" % r + " - %d" % abs(combo) + " = %d" % (r + combo))
        r += combo
    if((k - combo) <= 0):
        print("Ken: %d" % k + " - %d" % combo + " = %d" % (k - combo))
        k -= combo

#-------------------------------------------------------------------#
# concede 1 vitoria a quem ganhou o round1
if(r <= 0):
    vk = 1
else:
    vr = 1
# restaurar variaveis para o round2
r = 2000
k = 2000
combo = 0
x = 0
#-------------------------------------------------------------------#
# round2
while(r > 0 and k > 0):  # enquanto alguem nao fica sem vida
    x = int(input())  # lê um dano
    testarnum = 0  # variavel usada para testar a naturaza do dano lido
    ehperfeito = 0  # var p/ informar se o num eh perfeito ou nao

    # testar se ele eh perfeito
    if(abs(x) != 1):
        for i in range(1, abs(x)):
            if(x % i == 0):
                testarnum += i

    # se o num eh perfeito, o multiplicador de danos por 3 eh usado
    if(testarnum == abs(x)):
        x *= 3
        ehperfeito = 1

    # se o numero nao eh perfeito, ele ainda pode ser triangular
    if(ehperfeito == 0):
        testarnum = 0
        cont = 1
        while(testarnum <= abs(x)):  # testa se o num eh triangular
            testarnum += cont
            cont += 1
            if(testarnum == abs(x)):  # caso for triangular
                x *= 2  # atribui multiplicador de danos por 2
                break

    if(combo < 0 and x > 0):  # ryu levou dano
        print("Ryu: %d" % r + " - %d" % abs(combo) + " = %d" % (r + combo))
        r += combo
        combo = x
    elif(combo > 0 and x < 0):  # ken levou dano
        print("Ken: %d" % k + " - %d" % combo + " = %d" % (k - combo))
        k -= combo
        combo = x
    elif(combo >= 0 and x > 0 and (k - combo) > 0):  # continuando combo
        combo += x
    elif(combo <= 0 and x < 0 and (r + combo) > 0):  # continuando combo
        combo += x

    # verifica se o combo ja é capaz de derrotar um lutador
    #(impede chutar cachorro morto)
    if((r + combo) <= 0):
        print("Ryu: %d" % r + " - %d" % abs(combo) + " = %d" % (r + combo))
        r += combo
    if((k - combo) <= 0):
        print("Ken: %d" % k + " - %d" % combo + " = %d" % (k - combo))
        k -= combo

#-------------------------------------------------------------------#
# concede 1 vitoria a quem ganhou o round2
if(r <= 0):
    vk = vk + 1
else:
    vr = vr + 1
# verifica quem ganhou o combate ou se houve empate
if(vr == vk):
    print("empatou")
else:
    if(vr == 2):
        print("Ryu venceu")
    else:
        print("Ken venceu")
#-------------------------------------------------------------------#
