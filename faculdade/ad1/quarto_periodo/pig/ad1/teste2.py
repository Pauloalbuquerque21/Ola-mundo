import random



listas=[[],[],[],[],[],[],[],[],[]]
for c in range(0,9):
    for c2 in range(0,9):
        listas[c].append(".")
    

for c3 in listas:
    print(c3)

for c in range(0,9):
    lista_visual = ' '.join(listas[c])
    print(lista_visual)