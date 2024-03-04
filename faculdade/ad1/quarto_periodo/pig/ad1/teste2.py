import random

listas=[[],[],[],[],[],[],[],[],[]]

quantidade = 0

for c in range(0,9):
        if c == 0:#PRIMEIRA LINHA DO SUDUKO
            while True: # PRIMEIRA LINHA 
                if len(listas[0]) == 0:#Parte de ingluir o primeiro elemento 
                    aleatorio1 = random.randint(1,9)
                    listas[0].append(aleatorio1)
                else:#Parte de incluir os demais elementos para a linha
                    aleatorio1 = random.randint(1,9)
                    if aleatorio1 not in listas[0]:
                        listas[0].append(aleatorio1)
                    else:
                        print(f'já adicionado{c}')

                if len(listas[0]) == 9:
                    break
        else:#As DEMAIS LINHAS DO SUDOKU.
            quantidade += 1
            while True: #SEGUNDA LINHA.
                vezes = 0 #Quantidade de vezes que irá conferir na lista c, elemento 0.
                vezes2 = 0 #Quantidade de vezes que irá conferir na lista c, outros elementos.
                if len(listas[c]) == 0:
                    aleatorio1 = random.randint(1,9)
                    #verificar se a listas anteriores no elemento posição 0 existe elemento igual: 
                    for quant in range(quantidade-1,-1,-1):
                        if aleatorio1 != listas[quant][0]:
                            vezes += 1
                        else:
                            print(f'Já existe {aleatorio1}')
                    if  vezes == quantidade:
                        listas[c].append(aleatorio1)
                    else:
                        print(f'já adicionado {c}')

                #Adicionar os demais elementos:
                else:
                    print(listas)
                    aleatorio1 = random.randint(1,9)
                    print(f'{aleatorio1}')
                    for quant2 in range(quantidade-1,-1,-1):
                        if (aleatorio1 not in listas[c]) and (aleatorio1 != listas[quant2][len(listas[c])]):
                            vezes2 += 1
                            print(f'vezes:{vezes2}')
                            print(f'quantiadde:{quantidade}')
                            print(f'lista:{c}')
                            print(f'Valor aleatorio {aleatorio1}')
                    if vezes2 == quantidade:
                        print(f'adicionou {aleatorio1}')
                        listas[c].append(aleatorio1)
                    else:
                        print('já adicionado')

                if len(listas[c]) == 9:
                    break

print(f'Quantidade:{quantidade}')
for c1 in listas:
    print(c1)