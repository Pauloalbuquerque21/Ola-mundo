class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    #esse método nome se torno um variavel.
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    def get_name(self):
        return self._nome

    def get_idade(self):
        return 2022 - self._ano_nascimento
    
pessoa = Pessoa('GUilherme', 1994 )
#Perceba que quando você usar a idade e name concilidado com o property,ele vira uma propriedade e usamos ele como variavel
print(f'Nome: {pessoa.nome}\tIdade: {pessoa.idade}')
print(f'Nome: {pessoa.get_name()}\tIdade:{pessoa.get_idade()}')