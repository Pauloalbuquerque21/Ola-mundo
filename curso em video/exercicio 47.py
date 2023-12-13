from time import sleep
n1 = int(input('Digite o primeiro número, tem que ser número par:'))
n2 = int(input('Digite o último, tem que ser número:'))
for c in range(n1,n2,2):
    print(c, end='')