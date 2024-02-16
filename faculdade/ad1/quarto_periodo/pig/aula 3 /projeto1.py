
class franc():
    def __init__(self,numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'

    def __add__(self,other):
        lista = list()
        for c in range(2,10):
            while True:
                if (self.denominador % c == 0) or (other.denominador % c == 0):
                    if self.denominador % c == 0:
                        self.denominador = self.denominador / c
                    if other.denominador % c == 0:
                        other.denominador = other.denominador / c
                    lista.append(c)
                else:
                    break
        mmc = 1
        for dados in lista:
            mmc = mmc * dados
        self.numerador = self.numerador * (mmc / self.numerador)
        other.numerador = other.numerador * (mmc / self.numerador)
        
        return lista
    #def __iadd__(self,other):
    #    self.numerador += other
    #    self.denominador += other
    #    return self
    def __mul__(self,other):
        return f'{self.numerador * other.numerador},{self.denominador * other.denominador}'
    def __eq__(self,other):
        return f'{self.numerador == other.numerador and self.denominador == other.denominador}'

    #def __sub__(self,other):
    #    return f'{self.numerador - other.numerador}'
    
    
franc1 = franc(5,4)
franc2 = franc(5,10)
franc3 = franc(4,10)

result = franc1 + franc2
#result2 = franction1 + franction2 + franction3
result_mult = franc1 * franc2
result_eq = franc1 == franc2
print(franc1)
print(franc2)
print(franc3)

print(result)
#print(result2)
print(result_mult)
print(result_eq)