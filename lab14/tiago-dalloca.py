# RA 206341

# I'M AM THE DAC - Darth Sidious

ins = input().split(" ")
ras = []
ras = list(map(int, filter((lambda x: x != ""), ins)))
o = 0

while(True):
    args = input().split(" ")
    c = args[0]
    if c == "p":
        if len(ras) != 0:
            print(" ".join(map(str, ras)), end="")
            print(" ")
    elif c == "c":
        list.sort(ras)
        o = 1
    elif c == "d":
        list.sort(ras, reverse=True)
        o = -1
    elif c == "b":
        b = int(args[1])
        ll = []
        if o == 0:
            print("Vetor nao ordenado!")
        elif o == 1:
            i, f = (0, len(ras) - 1)
            while i <= f:
                m = (i + f) // 2
                ll.append(m)
                if ras[m] == b:
                    break
                elif ras[m] > b:
                    f = m - 1
                elif ras[m] < b:
                    i = m + 1
            print(" ".join(map(str, ll)), end="")
            print(" ")
            if ras[m] == b:
                print("%d esta na posicao: %d" % (b, m))
            else:
                print("%d nao esta na lista!" % (b))
        else:
            i, f = (0, len(ras) - 1)
            while i <= f:
                m = (i + f) // 2
                ll.append(m)
                if ras[m] == b:
                    break
                elif ras[m] < b:
                    f = m - 1
                elif ras[m] > b:
                    i = m + 1
            print(" ".join(map(str, ll)), end="")
            print(" ")
            if ras[m] == b:
                print("%d esta na posicao: %d" % (b, m))
            else:
                print("%d nao esta na lista!" % (b))
    elif c == "i":
        i = int(args[1])
        if len(ras) >= 150:
            print("Limite de vagas excedido!")
        elif i in ras:
            print("Aluno ja matriculado na turma!")
        else:
            ras.append(i)
            if o != 0:
                list.sort(ras, reverse=o < 0)
    elif c == "r":
        r = int(args[1])
        if len(ras) == 0:
            print("Nao ha alunos cadastrados na turma!")
        elif r not in ras:
            print("Aluno nao matriculado na turma!")
        else:
            ras.remove(r)
    else:
        break
