dados = [[],[]]
pares = []
impares= []
for c in range(0,7):
    valores=int(input(f'Digite o {c+1} valor:'))
    if valores % 2 == 0 :
        dados[0].append(valores)
    elif valores % 2 != 0:
        dados[1].append(valores)

print(f'PARES : {sorted(dados[0])}')
print(f'Impares: {sorted(dados[1])}')

