from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        self.get_ano_nascimento()

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    def identificacao(self,escola):
        print(f'Nome do aluno: {self.nome}\nIdade:{self.idade}\nEscola:{escola}')

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)

#p1 = Pessoa('Carlo',32)
#print(p1.get_ano_nascimento())
#p1.identificacao(input('Qual o nome da escola:'))
print(p1.nome, p1.idade)
#p1.get_ano_nascimento()
print(Pessoa.gera_id())
    
