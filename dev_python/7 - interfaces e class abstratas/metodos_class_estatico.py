class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    #O metodo de class, ja tem uma relação, mas perceba que retorna as variaveis nome e idade, para class usando o cls(convenção )
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    #metodo estático, percebe que ele está dentro da class, porém não tem uma relação, só quando é chamado.
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
#perceba que não precisa instância o objeto e depois usá-lo, mas sim vai direto.
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "guilherme")
print(p.nome, p.idade)
# como o método estático tbm
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))