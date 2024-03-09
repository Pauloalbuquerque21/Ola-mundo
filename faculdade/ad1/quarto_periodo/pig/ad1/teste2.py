import random

listas=[[],[],[],[],[],[],[],[],[]]
for c in range(0,9):
    for c2 in range(0,9):
        listas[c].append(".")
erros = 0
jogadas = 0

while True:#loop do jogo
    lista_visual = list()

    for c in range(0,9):
        lista_visual = ' '.join(listas[c])
        print(lista_visual)

    linha = int(input('Digite a linha:'))
    coluna = int(input('Digite a coluna:'))
    valor = str(input('digite o valor '))

    #veriaveis:
    confere_inferior = 0
    confere_superior = 0
    confere_linha = 0
    # conferir se está na linha:
    if valor not in listas[linha]:
        confere_linha += 1
    #verificar as linhas inferiores, mesma coluna:
    for quant2 in range(linha-1,-1,-1):
        if valor != listas[quant2][coluna]:
            confere_inferior += 1
    #verificar linhas superiores, da mesma coluna:
    for superior in range(linha+1,9):
        if valor != listas[superior][coluna]:
            confere_superior += 1
    
    if (confere_inferior == linha) and (confere_superior == (9-(linha+1))) and (confere_linha == 1):
        jogadas += 1
        print(f'adicionou {valor}')
        listas[linha][coluna] = valor
        if jogadas == 5:
            break
    else:

        print('já adicionado')

