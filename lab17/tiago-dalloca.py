# RA 206341 Tiago Pereira Dall'Oca

import re


class EmailInvalido(Exception):
    pass


class SenhaFraca(Exception):
    pass


class RAInvalido(Exception):
    pass


class Repositorio:
    def __init__(self):
        self.alunos = []
        self.regras_senha = [
            lambda s: any(x.isupper() for x in s),
            lambda s: len([x for x in s if x.islower()]) >= 2,
            lambda s: any(x in "!@#$&*" for x in s),
            lambda s: len(s) >= 8
        ]
        self.email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        if aluno.ra not in [a.ra for a in self.alunos]:
            if all(regra(aluno.senha) for regra in self.regras_senha):
                if re.match(self.email_regex, aluno.email):
                    self.alunos.append(aluno)
                else:
                    raise EmailInvalido
            else:
                raise SenhaFraca
        else:
            raise RAInvalido

    # Este método recebe o parâmetro aluno e altera, no repositório, os
    # dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        a = self.achaAluno(aluno.ra)
        a.__dict__ = aluno.__dict__

    # Este método recebe o parâmetro ra e deve retornar o aluno que possui
    # o RA informado como parâmetro
    def achaAluno(self, ra):
        for a in self.alunos:
            if a.ra == ra:
                return a
        raise RAInvalido

    # Este método recebe o parâmetro ra e deve remover o aluno
    # correspondente do repositório
    def remover(self, ra):
        nals = [a for a in self.alunos if a.ra != ra]
        if len(nals) == len(self.alunos):
            raise RAInvalido
        self.alunos = nals

        # Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.alunos = []
