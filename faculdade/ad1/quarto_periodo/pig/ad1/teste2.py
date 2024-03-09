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
    quadrado = 0
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
    #verificar os quadrados:
    #quadrado 1        
    if (linha <=2) and (coluna <=2):
        for linha_verif in range(0,3):
            for coluna_verif in range(0,3):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
    
    #quadrado 2
    elif (linha <= 2) and (3 <= coluna <=5):
        for linha_verif in range(0,3):
            for coluna_verif in range(3,6):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 3
    elif (linha <=2) and (6<=coluna <=8):
        for linha_verif in range(0,3):
            for coluna_verif in range(6,9):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 4
    elif (3<=linha <=5) and (coluna <=2):
        for linha_verif in range(3,5):
            for coluna_verif in range(0,3):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 5
    elif (3<=linha <=5) and (3 <= coluna <=5):
        for linha_verif in range(3,6):
            for coluna_verif in range(3,6):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 6
    elif (3<=linha <=5) and (6<=coluna <=8):
        for linha_verif in range(3,6):
            for coluna_verif in range(6,9):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 7
    elif (6<=linha <=8) and (coluna <=2):
        for linha_verif in range(6,9):
            for coluna_verif in range(0,3):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 8
    elif (6<=linha <=8) and (3 <= coluna <=5):
        for linha_verif in range(6,9):
            for coluna_verif in range(3,6):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     #quadrado 9
    elif (6<=linha <=8) and (6<=coluna <=8):
        for linha_verif in range(6,9):
            for coluna_verif in range(6,9):
                if valor == listas[linha_verif][coluna_verif]:
                    quadrado += 1
     

    if (confere_inferior == linha) and (confere_superior == (9-(linha+1))) and (confere_linha == 1) and (quadrado == 0):
        jogadas += 1
        print(f'adicionou {valor}')
        listas[linha][coluna] = valor
        
    else:

        print('já adicionado')

