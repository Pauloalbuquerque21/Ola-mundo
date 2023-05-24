#valores = [1,2,3,4,5,6,7,8,9]
#aut = []
#n1 = int(input('Quantos valores você quer sorteado:'))
#import random
#def alet(a):
#    for c in range(0,a):
#        aut.append(random.choice(valores))
#    print(f'São {a} valores sorteados, que são {aut}')
#
#def somapar(b):
#    result = vezes = 0 
#    for c in b:
#        if c % 2 ==0:
#            result = c + result
#            vezes +=1
#    print(f'Temos {vezes} numeros pares e a soma deles é igual a {result}')


#alet(n1)
#somapar(aut)

#Feito pelo professor

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end = '')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)