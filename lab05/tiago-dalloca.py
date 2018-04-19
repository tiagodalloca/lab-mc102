# RA 206341

# O jogo Street Fighter foi um dos primeiros jogos eletrônicos do gênero
# conhecido como jogos de luta. Neste jogo, um mestre de artes marciais,
# chamado Ryu, enfrenta outros lutadores em um torneio internacional de
# artes marciais. Cada combate entre Ryu e um oponente se dá em dois
# rounds. O objetivo é atacar o oponente com diferentes golpes, sendo que
# cada golpe aplicado subtrai uma certa quantidade de pontos de vida do
# outro combatente. Perde o round aquele jogador cujos pontos de vida
# ficar menor ou igual a zero primeiro. Vence a luta quem ganhar o maior
# número de rounds.

# o código é autoexplicativo


def read_int():
    return int(input())


ryu_hp = ken_hp = 50

game_round = 0

ryu_won_last_round = False

hit = read_int()
hit_sum = hit
while True:
    hit = read_int()
    if hit < 0:
        if hit_sum < 0:
            hit_sum += hit
        else:
            print('Ken:', ken_hp, '-', hit_sum, '=', ken_hp - hit_sum)
            ken_hp -= hit_sum
            hit_sum = hit
    else:
        if hit_sum >= 0:
            hit_sum += hit
        else:
            print('Ryu:', ryu_hp, '-', - hit_sum, '=', ryu_hp + hit_sum)
            ryu_hp += hit_sum
            hit_sum = hit

    rhp_plus_hs = ryu_hp + hit_sum
    khp_minus_hs = ken_hp - hit_sum
    if rhp_plus_hs <= 0:
        print('Ryu:', ryu_hp, '-', - hit_sum, '=', rhp_plus_hs)
        if game_round == 0:
            game_round += 1
            ryu_hp = ken_hp = 50
            hit = read_int()
            hit_sum = hit
        elif ryu_won_last_round:
            print('empatou')
            break
        else:
            print('Ken venceu')
            break
    elif khp_minus_hs <= 0:
        print('Ken:', ken_hp, '-', hit_sum, '=', khp_minus_hs)
        if game_round == 0:
            game_round += 1
            ryu_hp = ken_hp = 50
            ryu_won_last_round = True
            hit = read_int()
            hit_sum = hit
        elif ryu_won_last_round:
            print('Ryu venceu')
            break
        else:
            print('empatou')
            break
