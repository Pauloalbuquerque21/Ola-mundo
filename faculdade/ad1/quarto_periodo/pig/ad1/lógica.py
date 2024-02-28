import random

listas=[[],[],[],[],[],[],[],[],[],[],[]]
lista_ale = list()

clock = 0


for linhas in listas:#linhas
    clock +=1
    if (clock != 4) and (linhas != 8):
        while True:
            if len(lista_ale):
                aleatorio1 = random.randirt(1,9)
            else:
                aleatorio1 = random.randirt(1,9)
                if aleatorio1 in lista_ale:
                     pass
                else:
                     lista_ale.append(aleatorio1)
            if len(lista_ale) == 9:
                 break
                 

        for colunas in range(1,12):#colunas

                    for c3 in range(aleatorio1,aleatorio2):

    else:
        for c2 in range(1,12):
            c.append('-')
        print(c)