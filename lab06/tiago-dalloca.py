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

# o código é autoexplicativo e bem semelhante ao do lab05

from functools import reduce

# o read_hit lê um golpe e já o deixa agrega o combo


def read_hit():
    hit = int(input())
    combo = 1
    if is_perfect(abs(hit)):
        combo = 3
    elif is_triangular(abs(hit)):
        combo = 2
    return hit * combo

# retorna um gerador de lista que é preguiçosamente avaliado


def divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i


# reduz os divisores a uma soma
def is_perfect(n):
    return reduce((lambda x, y: x + y), divisors(n)) == n


def is_triangular(n):
    s = 1
    i = 2
    while s < n:
        s += i
        i += 1
    return s == n


# códgio quase idêntico ao lab05 a partir daqui

ryu_hp = ken_hp = 2000

game_round = 0

ryu_won_last_round = False

hit = read_hit()
hit_sum = hit

while True:
    hit = read_hit()
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
            ryu_hp = ken_hp = 2000
            hit = read_hit()
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
            ryu_hp = ken_hp = 2000
            ryu_won_last_round = True
            hit = read_hit()
            hit_sum = hit
        elif ryu_won_last_round:
            print('Ryu venceu')
            break
        else:
            print('empatou')
            break
