# thomas (Desnord)

# objetivo: criar um programa para gerenciar um repositório 
# de dados (base de dados) com registros acadêmicos de alunos.

# entrada: A primeira linha da entrada contém um inteiro n indicando o número máximo 
# de alunos que a base conterá.
# As linhas seguintes consistem de operações a serem realizadas na base de alunos.

# saída: Cada linha da saída do programa contém o resultado da
# execução de cada operação dada na entrada, de forma que 
# a saída possui uma linha a menos que a quantidade de linhas da entrada.

'''----------------------------------------------------------------------------------'''
class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass
    
class Repositorio:
    def __init__(self):
        self.alunos = []

    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        
        #verificando senha
        if len(aluno.senha) < 8:
            raise SenhaFraca

        TestaSenha = [0,0,0,0,0,0]

        for i in range(len(aluno.senha)):
            atual =str(aluno.senha[i])
            
            if atual.isalpha() and atual.isupper():
                TestaSenha[0] = 1
                
            if atual.isalpha() and atual.islower():
                if TestaSenha[1] != 1:
                    TestaSenha[1] = 1
                else:
                    TestaSenha[2] = 1

            if atual.isdigit():
                if TestaSenha[3] != 1:
                    TestaSenha[3] = 1
                else:
                    TestaSenha[4] = 1

            if atual == '@' or atual == '!' or atual == '#' or atual == '&' or atual == '$' or atual == '*':
                TestaSenha[5] = 1
                
        if TestaSenha.__contains__(0):
            raise SenhaFraca
        
        #-----------------

        '''verificando email'''
        usuario = ''
        servidor = ''
        dominio = ''
        aux = 0
        ignora = False

        for i in range(len(aluno.email)):
            atual = aluno.email[i]

            if atual == '@':
                aux = 1
                ignora = True
            
            elif (atual == '.' and aux == 1):
                aux = 2
                ignora = True

            if (aux == 0 and ignora == False):
                usuario += atual
            if (aux == 1 and ignora == False):
                servidor += atual
            if (aux == 2 and ignora == False):
                dominio += atual

            ignora = False

        if len(usuario) == 0 or len(servidor) == 0 or len(dominio) < 2 or len(dominio) > 4:
            raise EmailInvalido

        for i in range(len(usuario)):
            atual = usuario[i]

            if not atual.isdigit() and not atual.isalpha():
              if atual != '_' and atual != '.' and atual != '+' and atual != '-':
                  raise EmailInvalido

        for i in range(len(servidor)):
            atual = servidor[i]

            if not atual.isdigit() and not atual.isalpha():
                raise EmailInvalido

        for i in range(len(dominio)):
            atual = dominio[i]

            if not atual.isalpha():
                raise EmailInvalido
        
        '''-----------------'''

        #verifica se ra já está cadastrado
        for i in range(len(self.alunos)):
            if(self.alunos[i].ra == aluno.ra):
                raise RAInvalido
        #---------------------------------

        
        self.alunos.append(aluno)

    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        
        #verifica se o aluno existe no repositorio
        existe = False
        for i in range(len(self.alunos)):
            if self.alunos[i].ra == aluno.ra:
                existe = True
                break
        #-----------------------------------------

        if existe == False:
            raise RAInvalido

        #verificando senha
        if len(aluno.senha) < 8:
            raise SenhaFraca

        TestaSenha = [0,0,0,0,0,0]

        for i in range(len(aluno.senha)):
            atual =str(aluno.senha[i])
            
            if atual.isalpha() and atual.isupper():
                TestaSenha[0] = 1
                
            if atual.isalpha() and atual.islower():
                if TestaSenha[1] != 1:
                    TestaSenha[1] = 1
                else:
                    TestaSenha[2] = 1

            if atual.isdigit():
                if TestaSenha[3] != 1:
                    TestaSenha[3] = 1
                else:
                    TestaSenha[4] = 1

            if atual == '@' or atual == '!' or atual == '#' or atual == '&' or atual == '$' or atual == '*':
                TestaSenha[5] = 1
                
        if TestaSenha.__contains__(0):
            raise SenhaFraca
        
        #-----------------

        '''verificando email'''
        usuario = ''
        servidor = ''
        dominio = ''
        aux = 0
        ignora = False

        for i in range(len(aluno.email)):
            atual = aluno.email[i]

            if atual == '@':
                aux = 1
                ignora = True
            
            elif (atual == '.' and aux == 1):
                aux = 2
                ignora = True

            if (aux == 0 and ignora == False):
                usuario += atual
            if (aux == 1 and ignora == False):
                servidor += atual
            if (aux == 2 and ignora == False):
                dominio += atual

            ignora = False

        if len(usuario) == 0 or len(servidor) == 0 or len(dominio) < 2 or len(dominio) > 4:
            raise EmailInvalido

        for i in range(len(usuario)):
            atual = usuario[i]

            if not atual.isdigit() and not atual.isalpha():
              if atual != '_' and atual != '.' and atual != '+' and atual != '-':
                  raise EmailInvalido

        for i in range(len(servidor)):
            atual = servidor[i]

            if not atual.isdigit() and not atual.isalpha():
                raise EmailInvalido

        for i in range(len(dominio)):
            atual = dominio[i]

            if not atual.isalpha():
                raise EmailInvalido
        
        '''-----------------'''
        
        # caso passar pela verificacao de email, de senha e o ra existir no repositorio
        for i in range(len(self.alunos)):
            
            #atualizar os dados
            if self.alunos[i].ra == aluno.ra:
               self.alunos[i] = aluno
               break 

    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        
     for i in range(len(self.alunos)):
         # se achar o aluno do ra buscado
         if self.alunos[i].ra == ra:
             return self.alunos[i]
        
         # se o ra buscado nao está no repositório
         elif self.alunos[i].ra != ra and i == len(self.alunos)-1:
             raise RAInvalido 

    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        
     # se nenhum ra estiver cadastrado  
     if len(self.alunos) == 0:
         raise RAInvalido

     for i in range(len(self.alunos)):
         # se achar o ra buscado
         if self.alunos[i].ra == ra:
            del self.alunos[i]
            break
        # se o ra buscado não está no repositório
         if (self.alunos[i].ra != ra and i == len(self.alunos)-1):
            raise RAInvalido
         

    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
     self.alunos.clear



'''--------------------------------------------------------------------------------------------------------'''
