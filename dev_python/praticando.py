#vou criar um banco

class Bradesco:
    def __init__(self,conta,saldo):
        self.conta = conta
        self._saldo = saldo
    
    def depositar(self,valor):
        self._saldo +=valor
        return self._saldo
    
    def saldo(self):
        print(f'A conta:{self.conta}\nSaldo atual:{self._saldo}')
    

class Brasil(Bradesco):
    def sacar(self,valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return self._saldo      
        else:
            print('valor dp saldo insulficiente para essa transação')  


conta_bradesco = Bradesco(1234,100)
conta_brasil = Brasil(2345,200)

conta_bradesco.depositar(100)
conta_bradesco.saldo()

    