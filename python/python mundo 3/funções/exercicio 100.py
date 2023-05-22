valores = [1,2,3,4,5,6,7,8,9]
aut = []
n1 = int(input('Quantos valores você quer sorteado:'))
import random
aut.clear()
for c in range(0,n1):
    aut.append(random.choice(valores))

print(f'{aut}')