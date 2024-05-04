#class pai
class Veiculo:
                    #argumentos     
    def __init__(self,cor,placa,numero_rodas):
        #atributos
        self.cor = cor
        self.placa = placa
        self.numero = numero_rodas
    def ligar_motor(self):
        print("Ligar o motor")

#classes filhas 
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    def __init__(self,cor,placa,numero_rodas,Carregamento):
        #sobrescrever

        #primeira forma:
        #self.cor = cor
        #self.placa = placa
        #self.numero = numero_rodas

        #segunda forma:
        #super().__init__(cor,placa,numero_rodas)

        self.Carregamento = Carregamento
    def esta_carregado(self):
        print(f"{'Sim' if self.Carregamento else 'Não'} estou carregamento")

class Caminhao(Veiculo):
    pass

moto = Motocicleta("azul",'1234',2)
carro = Carro("vermelho",'2345',4,False)

carro.ligar_motor()
moto.ligar_motor()

carro.esta_carregado()

