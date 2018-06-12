# thomas (Desnord)

# objetivo: calcular a media final de um aluno

# entrada: nota da prova 1, nota da prova2,
# media ponderada dos laboratorios e caso o aluno fez exame
# pega a nota do exame

# saida: media das provas, media antes do exame e nota final

p1 = float(input())  # pega nota da p1
p2 = float(input())  # pega nota da p2
ml = float(input())  # pega media ponderada dos laboratorios

mp = (2 * p1 + 3 * p2) / 5  # calcula media das provas
m = 0
f = 0
if(mp < 5 or ml < 5):
    # se a media das provas ou dos laboratorios for menor do que 5
    m = min(mp, 4.9)  # calcula a media antes do exame
    if(m > 2.5):  # se o aluno pode fazer exame
        e = float(input())  # pega a nota do exame
        f = (m + e) / 2  # calcula a media final
    else:  # caso o aluno nao tenha media para fazer o exame
        f = m  # calcula a nota final
else:
    # caso o aluno nao pegou exame
    m = (3 * mp + 2 * ml) / 5  # calcula a media antes do exame
    f = m  # calcula a nota final


print("%.1f" % mp)  # mostra a media das provas
print("%.1f" % m)  # mostra a media antes do exame
print("%.1f" % f)  # mostra a nota final
