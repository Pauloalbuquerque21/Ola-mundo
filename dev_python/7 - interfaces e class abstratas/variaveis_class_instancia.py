class Estudante:
    #Variavel de class
    escola = "DIO"

    def __init__(self,nome, matricula):
        #variavel de instância
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
#Esse "*" tem como função aceitar uma quantidade indeterminada de objetos
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('GUilherme', 2)


print(aluno_1)
print(aluno_2)


mostrar_valores(aluno_1, aluno_2)
#vocÊ está alterando a variavel da class, logo irá modificar em todos os objetos.
Estudante.escola = "Python"
#vOCÊ ATÉ CONSEGUE modificar um objeto, mas ela é uma variavel de class
aluno_1.escola = "DIO"
#essa variavel é de instância, logo para você modificar terá que chamar o objeto e só modificarar naquela objeto espefífico.
Estudante.nome = "carlos"
Aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2)


