from aluno import Aluno
from lab17 import Repositorio
from lab17 import EmailInvalido
from lab17 import SenhaFraca
from lab17 import RAInvalido
import sys
import os
sys.path.insert(0, os.getcwd())

linha = input()

repositorio = Repositorio()
while linha != "q":
    dados = linha.split(" ")
    if dados[0] == ">":
        try:
            aluno = repositorio.achaAluno(dados[1])
            print(
                "%s - %s - %s - %s" %
                (aluno.ra,
                 aluno.email,
                 aluno.nome,
                 aluno.usuario))
        except RAInvalido:
            print("Aluno %s não encontrado" % dados[1])
    elif dados[0] == "+":
        try:
            aluno = Aluno(' '.join(dados[5:]),
                          dados[1], dados[2], dados[3], dados[4])
            repositorio.adicionar(aluno)
            print("Adicionado: %s - %s - %s - %s" %
                  (aluno.ra, aluno.email, aluno.nome, aluno.usuario))
        except RAInvalido:
            print("Aluno %s não encontrado" % dados[1])
        except SenhaFraca:
            print("Aluno não inserido, senha fraca fornecida")
        except EmailInvalido:
            print("Aluno não inserido, email inválido")
    elif dados[0] == "*":
        try:
            aluno = Aluno(' '.join(dados[5:]),
                          dados[1], dados[2], dados[3], dados[4])
            repositorio.alterar(aluno)
            print("Alterado: %s - %s - %s - %s" %
                  (aluno.ra, aluno.email, aluno.nome, aluno.usuario))
        except RAInvalido:
            print("Aluno %s não encontrado" % dados[1])
        except SenhaFraca:
            print("Aluno não alterado, senha fraca fornecida")
        except EmailInvalido:
            print("Aluno não alterado, email inválido")
    elif dados[0] == "-":
        try:
            repositorio.remover(dados[1])
            print("Aluno %s removido com sucesso" % dados[1])
        except RAInvalido:
            print("Aluno %s não encontrado" % dados[1])
    linha = input()

repositorio.limparRepositorio()
