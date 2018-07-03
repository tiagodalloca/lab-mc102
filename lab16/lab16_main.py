#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.getcwd())
import lab16 as lab


# Le string a ser procurada

busca = input()
buscaOriginal = busca[:]

aux = input()

token = aux.split()
palavrasIgnorar = token

# le numero de paginas
numeroPaginas = int(input())

palavrasPagina = []
# Le palavras em cada página
for pag in range(0, numeroPaginas):
    palavrasPagina.append(input())

# leitura dos links
links = [[0 for j in range(numeroPaginas)] for i in range(numeroPaginas)]

# le links
numeroLinks = int(input())

for i in range(numeroLinks):
    linha = input()
    pos = [int(i) for i in linha.split()]
    links[pos[0]][pos[1]] = 1

# processa para retirar palavras nao importantes
busca = lab.removePalavras(busca, palavrasIgnorar)

# Informacoes na saida
print("Termo a ser buscado: %s" % buscaOriginal)
print("Termo a ser buscado processado: %s" % busca)

# transforma busca em array de palavras
if busca is not None:
    busca = busca.split()
numeroPalavrasBuscadas = 0

# verifica quais palavras-chaves estao em quais paginas
paginasTemPalavrasChave = lab.pagsResposta(palavrasPagina, busca)

#  calcula numero de links por pagina
numeroLinksPorPagina = lab.linksResposta(links, paginasTemPalavrasChave)

for p in range(len(numeroLinksPorPagina)):
    if numeroLinksPorPagina[p] == -1:
        print("Pagina %d: nao encontrado" % p)
    else:
        print(
            "Pagina %d: encontrado/%d links" %
            (p, numeroLinksPorPagina[p]))
