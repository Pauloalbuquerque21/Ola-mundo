class Bradesco:
    def __init__(self,conta,saldo):
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo +=valor
        print(f'A conta:{self.conta}\nSaldo atual:{self.saldo}')


conta1 = Bradesco(1234,100)
conta1.saldo = 300
conta1.depositar(100)