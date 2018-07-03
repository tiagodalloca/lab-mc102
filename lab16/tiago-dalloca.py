# RA 206341

from functools import reduce


#  Funcao: removePalavras
#
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: lista de strings com as palavras a serem removidas
#
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.


def removePalavras(s, vs):
    return " ".join(list([w for w in s.split() if w not in vs]))

#  Funcao: pagsResposta
#
# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#	Deve verificar se cada página em paginas contém todos os termos
#	de busca em termosBusca. Se a paginas[i] contiver todos os termos
#	então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#	menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.


def pagsResposta(palavrasPagina, termosBusca):
    return list(map((lambda p: 1 if all(tb in p for tb in termosBusca) else 0),
                    map(lambda x: x.split(), palavrasPagina)))


#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links, resp):
    return [reduce(lambda a, x: a + 1 if resp[x[0]] == 1 and x[1][i] == 1
                   else a, enumerate(links), 0)
            if resp[i] == 1
            else -1 for i in range(len(links))]
