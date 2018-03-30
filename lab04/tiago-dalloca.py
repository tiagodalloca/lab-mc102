# RA 206341

# Super controlador de estacionamentooooo


def read_int():
    # funçãozona pra ler inteiros
    return int(input())


# capacidade
C = read_int()

# entrada imediata do input
i = read_int()

# o resto é autoexplicativo
while i != 0:
    if C - i < 0:
        print("Veiculo muito grande! Capacidade restante:", C)
    else:
        C -= i
        if i > 0:
            print("Seja bem-vindo! Capacidade restante:", C)
        else:
            print("Volte sempre! Capacidade restante:", C)
    i = read_int()
