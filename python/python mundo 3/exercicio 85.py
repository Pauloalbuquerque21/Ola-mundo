dados = []
pares = []
impares= []
for c in range(0,7):
    valores=int(input('Digite um valor:'))
    if valores % 2 == 0 :
        pares.append(valores)
    elif valores % 2 != 0:
        impares.append(valores)
dados.append(pares[:])
pares.clear
dados.append(impares[:])
impares.clear

for c in dados[0]:
    print(f'Pares {c}')
for c in dados[1]:
    print(f'Impares {c}')

