

class desconto2:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - ((self.preco*percentual)/100)
        print(f'{self.preco}')
    def nome_minusculo(self):
        self.nome = self.nome.lower()
        print(f'{self.nome}')

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preco = valor    
        

p1 = desconto2('CARLOS',12)
p1.desconto(30)
p1.nome_minusculo()

p2 = desconto2('AMANDA','R$20')
p2.desconto(10)


