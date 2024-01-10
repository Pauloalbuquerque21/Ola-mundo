class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nome} está falando ....({self.nomeclasse})')

class cliente(Pessoa):
    def comprar(self, x):
        print(f'{self.nome} quer comprar {x}')

class funcionario(Pessoa):
    def vender (self,x):
        print(f'{self.nome} ira vernder {x}')

