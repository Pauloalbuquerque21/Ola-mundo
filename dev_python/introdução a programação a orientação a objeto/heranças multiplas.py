
#CLASS PAI
class Animal:
    def __init__(self, nro_patas,dentes):
        self.nro_patas = nro_patas
        self.dentes = dentes
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#class
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self,**kw):
    #def __init__(self, cor_bico, cor_pelo, nro_patas,**kw):
        #super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        super().__init__(**kw)

gato = Gato(nro_patas=4, cor_pelo="Preto", dentes = 4)
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja", dentes = 5)
print(ornitorrinco)