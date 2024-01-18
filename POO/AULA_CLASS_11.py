from dataclasses import dataclass

class Person:
    def __init__(self,name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name__}'\
        f'({self.name} {self.lastname})'
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, o):
        return self.lastname == o.lastname
    
    @dataclass
    class person:
        name: str
        lastname: str
    
if __name__ == '__main__':
    john1 = Person('John', 'Doe')
    john2 = Person('John1','Doe')
    mary = Person('Mary','Jane')
    