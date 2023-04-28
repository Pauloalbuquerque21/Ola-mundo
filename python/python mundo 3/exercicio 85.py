dados = []
pares = []
impares= []
for c in range(0,7):
    valores=int(input('Digite um valor:'))
    if valores % 2 == 0 :
        pares.append(valores)
    else:
        impares.append(valores)
    
print(f'Impares:{sorted(impares)}')
print(f'Pares {sorted(pares)}')

