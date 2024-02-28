import random
lista_ale = list()

while True:
    if len(lista_ale) == 0:
        aleatorio1 = random.randint(1,9)
        lista_ale.append(aleatorio1)
        print(aleatorio1)
    else:
        aleatorio1 = random.randint(1,9)
        print(aleatorio1)
        if aleatorio1 not in lista_ale:
            lista_ale.append(aleatorio1)
        else:
            print('já adicionado')

    if len(lista_ale) == 9:
        break

print(lista_ale)