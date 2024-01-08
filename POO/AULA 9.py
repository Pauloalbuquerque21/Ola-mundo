from AULA_CLASS_9 import Endereco, Cliente

cliente1 = Cliente('Paulo','32')
cliente1.insere_endereco('Rio de janeiro','RJ')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Carlos', '18')
cliente2.insere_endereco('Vitoria','ES')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João','16')
cliente3.insere_endereco('Salvador','Ba')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('################################################')