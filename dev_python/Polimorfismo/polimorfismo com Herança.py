class Passaro:
    def voar(self):
        print("Voando...")

class Galinha(Passaro):
    def voar(self):
        print("Galinha gostaria:")
        super().voar()
    
class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

p1 = Avestruz()
p2 = Pardal()
p3 = Galinha()


#Polimorfismo seria pegar várias CLass e criar um método em cada class com o mesmo nome, por exemplo o "voar". Mesmo nome, mas dependendo do objeto ter um efeito diferênte0
p2.voar()
p1.voar()
p3.voar()
