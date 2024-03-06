import random

listas=[[],[],[],[],[],[],[],[],[]]

for c in range(0,9):
    for c2 in range(0,9):
        listas[c].append(2)
quantidade = 0

linha = int(input('Digite a linha:'))
coluna = int(input('Digite a coluna:'))
valor = int(input('digite o valor '))


confere = 0
aleatorio1 = valor
for quant2 in range(linha-1,-1,-1):
    if (aleatorio1 not in listas[linha]) and (aleatorio1 != listas[quant2][coluna]):
        confere += 1
if confere == linha:
    print(f'adicionou {aleatorio1}')
    listas[linha][coluna] = aleatorio1
else:
    print('já adicionado')


for c1 in listas:
    print(c1)