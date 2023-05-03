from time import sleep
import random
lista = []
for c in range(0,100):
    lista.append(c)
aut = random.choice(lista)
print('-'*15)
print('JOGA NA MEGA SENA')
print('-'*15)
quant = int(input('QUnatos jogos você quer que eu sorteie?'))

print(f'-=-=-=-=-= SORTEANDO {quant} JOGOS -=-=-=-=-=')
for c in range(0,quant):
    print(f'\nJogo {c+1}:',end='')
    for c in range(0,6):
        n1 = random.choice(lista)
        print(f'[{n1:^3}]',end='')
    sleep(1)
#print('\n-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')