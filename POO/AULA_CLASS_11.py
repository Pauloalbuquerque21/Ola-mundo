class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def print(self):
        print(f'Nome: {self.nome} \nidade: {self.idade}')