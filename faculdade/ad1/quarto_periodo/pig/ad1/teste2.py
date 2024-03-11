import random
lista_colunas = list()
for c in range(0,9):
    for c2 in range(0,4):
        lista_colunas.append(random.randint(1, 9))

print(lista_colunas)