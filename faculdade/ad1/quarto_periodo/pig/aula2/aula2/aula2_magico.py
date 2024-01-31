class dado():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a},{self.b}'
    def __add__(self,other):
        return f'{self.a+other.a}, {self.b + other.b}'

p1 = dado(1,2)
p2 = dado(2,3)

resultado = p1 + p2
print(resultado)