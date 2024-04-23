class casa:
    def __init__(self,porta,janela):
        self.porta = porta
        self.porta = janela
    
    def _str_(self):
        return f'{self.__class__.__name__}:{f'{chave}={valor}' for chave, valor in self.__dict__.items()}'

class badroom_broder(casa):
    def __ini__(self,armario,cama):
        self.armario = armario
        self.cama = cama
    



familia = (2,2)
print(casa)