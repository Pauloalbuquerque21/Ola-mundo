import random
print('Valores sorteados:')
lista = []
jogadores = {}
for c in range(0,10):
    lista.append(c)

for k in range(1,5):
    n1 = random.choice(lista)
    jogadores[k]=n1
    print(f'jogador{k} tirau {jogadores[k]}')

print('-='*30)
print('== RANKING DOS JOGADORES ==')


