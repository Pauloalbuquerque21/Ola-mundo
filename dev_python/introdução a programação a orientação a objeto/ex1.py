class bicicleta:
    def __init__(self,cor,modelo,ano,valor,status=True):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.status = status
    def parar(self):
        if self.status:
            self.status = False
            print('Bicicleta se encontra parada')
        else:
            print('Bicicleta já te encontra parada')
    def correr(self):
        if self.status:
            print('Bicicleta já se encontra em movimento ')
        else:
            self.status = True
            print('Iniciand a correr')



b1 = bicicleta('vermelho','Caloi','2022',300)

print(b1.cor)
print(b1.status)
b1.parar()
print(b1.status)
b1.parar()