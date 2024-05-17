class conta():
    def __init__(self,saldo,numero,agencia,cliente,historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo2(self):
        return self._saldo
    
    def novo_cliente(self):
        print(f'CLiente:{self._cliente}\nNúmero da conta:{self._numero}')

    def sacar(self,valor):
        if valor < self._saldo:
            self._saldo -= valor
            return True
        else:
            return False
        
    def depositar(self,valor):
        if valor > 0 :
            self._saldo += valor
            return True
        else:
            return False
#obs: quando você usa o **kw você tem que definir os atributos      
class conta_corrente(conta):
    def __init__(self,limites,limites_saques,**kw):
        self.limites = limites
        self.limites_saques=limites_saques
        super().__init__(**kw)
        


cliente = conta(200,1,2,'Carlos',1)

#print(cliente._saldo)

print(cliente.saldo2())
cliente.novo_cliente()
print(cliente.sacar(100))
print(cliente.saldo2())
cliente.depositar(500)
print(cliente.saldo2())

print('Cliente 2:')
cliente2 = conta_corrente(limites=1000,limites_saques=100,saldo=200,numero=1,agencia=3,cliente='Paulo',historico=1)
cliente2.novo_cliente()

