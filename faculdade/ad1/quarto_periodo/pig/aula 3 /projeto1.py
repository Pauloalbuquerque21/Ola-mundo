
class franctions:
    def __int__(self,numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __add__(self,other):
        return f'{self.numerador + other.numerador},{self.denominador + other.denominador}'
    
franction1 = franctions(2,4)
franction2 = franctions(5,10)

result = franction1 + franction2
print(result)