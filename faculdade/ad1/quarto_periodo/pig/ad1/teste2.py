import random

listas=[[],[],[],[],[],[],[],[],[]]
for c in range(0,9):
    for c2 in range(0,9):
        listas[c].append(".")
erros = 0
jogadas = 0

while True:
    lista_visual = list()

    for c in range(0,9):
        lista_visual = ' '.join(listas[c])
        print(lista_visual)

    linha = int(input('Digite a linha:'))
    coluna = int(input('Digite a coluna:'))
    valor = str(input('digite o valor '))


    confere = 0
    aleatorio1 = valor
    for quant2 in range(linha-1,-1,-1):
        if (aleatorio1 not in listas[linha]) and (aleatorio1 != listas[quant2][coluna]):
            confere += 1
    if confere == linha:
        jogadas += 1
        print(f'adicionou {aleatorio1}')
        listas[linha][coluna] = aleatorio1
        if jogadas == 5:
            break
    else:

        print('já adicionado')

