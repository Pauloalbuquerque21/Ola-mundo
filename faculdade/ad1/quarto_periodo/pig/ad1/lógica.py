import random

listas=[[],[],[],[],[],[],[],[],[],[],[]]
lista_1 = list()
lista_2 = list()

clock = 0
while True: # PRIMEIRA LINHA 
    if len(lista_1) == 0:
        aleatorio1 = random.randint(1,9)
        lista_1.append(aleatorio1)
    else:
        aleatorio1 = random.randint(1,9)
        if aleatorio1 not in lista_1:
            lista_1.append(aleatorio1)
        else:
            print('já adicionado')

    if len(lista_1) == 9:
        break
while True: # SEGUNDA LINHA 
    if len(lista_2) == 0:
        aleatorio1 = random.randint(1,9)
        if aleatorio1 != lista_1[0]:
            lista_2.append(aleatorio1)
            print(aleatorio1)
        else:
            print('termino')
    else:
        aleatorio1 = random.randint(1,9)
        print(aleatorio1)
        if (aleatorio1 not in lista_2) and (aleatorio1 != lista_1[len(lista_2)]):
            lista_2.append(aleatorio1)
        else:
            print('já adicionado')
        print(lista_2)

    if len(lista_2) == 9:
        break


print(f'lista1:{lista_1}')
print(f'Lista2:{lista_2}')










#for linhas in listas:#linhas
#    clock +=1
#    if (clock != 4) and (linhas != 8):
#        while True:
#            if len(lista_ale):
#                aleatorio1 = random.randirt(1,9)
#            else:
#                aleatorio1 = random.randirt(1,9)
#                if aleatorio1 in lista_ale:
#                     pass
#                else:
#                     lista_ale.append(aleatorio1)
#            if len(lista_ale) == 9:
#                 break
                 

#        for colunas in range(1,12):#colunas

#                    for c3 in range(aleatorio1,aleatorio2):

#    else:
#        for c2 in range(1,12):
#            c.append('-')
#        print(c)