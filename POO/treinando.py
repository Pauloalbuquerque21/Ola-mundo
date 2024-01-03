
class acao:
    def __init__(self, nome, idade, run=False):
        self.nome = nome
        self.idade = idade
        self.run = run
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,valor):
        if valor is not int:
            valor = int(valor)
        self._idade = valor 
    def corre(self,quant):
        print(f'{self.nome} começou a corre, e irá corre por {quant} minutos')
    def nascimento(self,atual):
        print(f'Como estamos no ano {atual}, então {atual - self.idade}')



