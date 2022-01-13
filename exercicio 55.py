maior = 0
menor = 0
for c in range(1,6):
    n1 = float(input(f'Peso da {c} pessoa:'))
    if c == 1:   
        maior = c
        menor = c
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print(f'O Maior peso é {maior}')
print(f'O menor peso é {menor}')


