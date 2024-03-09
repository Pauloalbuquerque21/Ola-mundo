def suduku_pricipal():
    listas=[[],[],[],[],[],[],[],[],[]]
    for c in range(0,9):
        for c2 in range(0,9):
            listas[c].append(".")
    return listas

lista = suduku_pricipal()
for c in lista:
    print(c)
