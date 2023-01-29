import random
n1 = int(input('Teste 1:'))
n2 = int(input('Teste 2:'))
n3 = int(input('Teste 3:'))
n4 = int(input('Teste 4:'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
n5 = n1 + n2 + n3 + n4
print('O número da escola é \n{}'.format(lista))
print(lista)