class Foo:
    def __init__(self, x = None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    #isso não é um método, quando usamos o setter vira uma variavel e atribui valor e não retorna
    @x.setter
    def x(self, value):
        self._x += value

    #não retorna 
    @x.deleter
    def x(self):
        self._x = 0 


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)    
