
class franc():
    def __init__(self,numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self):
        return f'{self.numerador}/{self.denominador}'
    def mmc(self,valor1,valor2):
        lista = list()
        denominador1 = valor1
        denominador2 = valor2
        for c in range(2,10):
            while True: #parte que pegamos os valores do mmc
                if (denominador1 % c == 0) or (denominador2 % c == 0):
                    if denominador1 % c == 0:
                        denominador1 = denominador1 / c
                    if denominador2 % c == 0:
                        denominador2 = denominador2 / c
                    lista.append(c)
                else:
                    break
        mmc = 1
        for dados in lista:#soma dos valores do mmc
            mmc = mmc * dados
            return mmc

    def __add__(self,other):#adição de franções
        lista = list()
        denominador1 = self.denominador
        denominador2 = other.denominador
        numerador1 = 0 #criei essa variavel, pois não quero comprometer os valores do self.numerador e other
        numerador2 = 0
        for c in range(2,10):
            while True: #parte que pegamos os valores do mmc
                if (denominador1 % c == 0) or (denominador2 % c == 0):
                    if denominador1 % c == 0:
                        denominador1 = denominador1 / c
                    if denominador2 % c == 0:
                        denominador2 = denominador2 / c
                    lista.append(c)
                else:
                    break
        mmc = 1
        for dados in lista:#soma dos valores do mmc
            mmc = mmc * dados
        numerador1 = self.numerador * (mmc / self.denominador)
        numerador2 = other.numerador * (mmc / other.denominador)
        
        return f'{(numerador1+numerador2)} /{mmc}'
    #def __iadd__(self,other):
    #    self.numerador += other
    #    self.denominador += other
    #    return self
    def __mul__(self,other):
        print(f'{self.numerador},{other.numerador}')
        return f'{self.numerador * other.numerador}/{self.denominador * other.denominador}'
    def __eq__(self,other):
        return f'{self.numerador == other.numerador and self.denominador == other.denominador}'

    def __sub__(self,other):
        return f'{self.numerador - other.numerador}'
    
    
franc1 = franc(5,4)
franc2 = franc(5,10)
franc3 = franc(4,10)

print(franc1)
print(franc2)
print(franc3)

result_soma = franc1 + franc2
#result2 = franction1 + franction2 + franction3
result_mult = franc1 * franc2
result_eq = franc1 == franc2

print(result_soma)
print(result_mult)
print(result_eq)
print(franc1.mmc(4,5))