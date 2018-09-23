# thomas (Desnord)

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
 sVet = s.split()
 for i in range(len(vs)):
  while(vs[i] in sVet):
   sVet.remove(vs[i])

 return ' '.join(map(str, sVet))

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

    ret = []

    for i in range(len(palavrasPagina)):
     atual = palavrasPagina[i].split()

     for j in range(len(termosBusca)):
      if(not termosBusca[j] in atual):
         ret.append(0)
         break

      if(j == len(termosBusca)-1):
         ret.append(1)

    return ret

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

def linksResposta(links,resp):
    numLinks = []

    for i in range(len(links)):
     if(resp[i] == 1):
      qtde = 0
      for j in range(len(links)):
       if(resp[j] != 0 and links[j][i] == 1):
        qtde += 1

      numLinks.append(qtde)

     else:
      numLinks.append(-1)

    return numLinks


