from time import sleep
import random
lista = []
random.choice(lista)
for c in range(0,100):
    lista.append(c)
aut = random.choice(lista)
print('-'*15)
print('JOGA NA MEGA SENA')
print('-'*15)
quant = int(input('QUnatos jogos você quer que eu sorteie?'))

print('-=-=-=-=-= SORTEANDO 5 JOGOS -=-=-=-=-=')
for c in range(0,quant):
    print(f'Jogo {c}: {aut}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
print(aut)