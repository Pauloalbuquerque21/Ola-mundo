import random

listas=[[],[],[],[],[],[],[],[],[]]

for c in range(0,9):
        if c == 0:#PRIMEIRA LINHA DO SUDUKO
            while True: # PRIMEIRA LINHA 
                if len(listas[0]) == 0:
                    aleatorio1 = random.randint(1,9)
                    listas[0].append(aleatorio1)
                else:
                    aleatorio1 = random.randint(1,9)
                    if aleatorio1 not in listas[0]:
                        listas[0].append(aleatorio1)
                    else:
                        print(f'já adicionado{c}')

                if len(listas[0]) == 9:
                    break
        elif 0 < c < 9:#as DEMAIS LINHAS DO SUDOKU
            while True: # SEGUNDA LINHA 
                if len(listas[c]) == 0:
                    aleatorio1 = random.randint(1,9)
                    if aleatorio1 != listas[c-1][0]:
                        listas[c].append(aleatorio1)
                        print(aleatorio1)
                    else:
                        print('termino')
                else:
                    aleatorio1 = random.randint(1,9)
                    print(aleatorio1)
                    if (aleatorio1 not in listas[c]) and (aleatorio1 != listas[c-1][len(listas[c])-1]):
                        listas[c].append(aleatorio1)
                    else:
                        print('já adicionado')

                if len(listas[c]) == 9:
                    break


for c1 in listas:
    print(c1)