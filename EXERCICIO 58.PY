import random
lista = [1,2,3,4,5,6,7,8,9,10]
escolha = random.choice(lista)
print(escolha)
n1 = int(input('Qual Valor o computador escolheu entre 1 e 10:'))
while escolha != n1:
    if n1 < escolha:
        n1 = int(input('É maior .... escolha:'))
    elif n1 > escolha:
        n1 = int(input('É menor .... escolha:'))