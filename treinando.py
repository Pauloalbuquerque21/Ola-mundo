a = 10
b = 4
lista = list()
for c in range(2,10):    
    while True:
        if (a % c == 0) or (b % c == 0):
            if a % c == 0:
                a = a / c
                print(a)
            if b % c == 0:
                print(b) 
                b = b / c
            lista.append(c)
        else:
            break
mmc = 1
for dados in lista:
    mmc = mmc * dados




print(lista)
print(mmc)
