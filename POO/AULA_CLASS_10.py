class Pessoa:
    #def __init__(self,nome,idade):
    #    self.nome = nome 
    #    self.idade = idade
    #    self.nomeclasse = self.__class__.__name__
    def falar(self):
        return 3

class cliente(Pessoa):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def comprar(self, x):
        print(f'{self.nome} quer comprar {self.falar()**2}, {x}')

class funcionario(Pessoa):
    def vender (self,x):
        print(f'{self.nome} ira vernder {x}')

