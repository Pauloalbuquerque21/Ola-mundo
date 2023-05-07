#import random
#from time import sleep
#print('Valores sorteados:')
#lista = []
#jogadores = {}
#ranking=dict()
#for c in range(1,5):
#    lista.append(c)

#for k in range(1,6):
#    n1 = random.choice(lista)
#    jogadores[k]=n1
#    print(f'jogador{k} tirau {jogadores[k]}')
#    sleep(1)
#ranking = sorted
#print(f'{jogadores}')
#print('-='*30)
#print('== RANKING DOS JOGADORES ==') 
from random import randint
from time import sleep
from operator import itemgetter 
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)
        }
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)


