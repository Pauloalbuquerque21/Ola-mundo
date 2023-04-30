matriz = [[0,0,0],[0,0,0],[0,0,0]]
resul = 0
menor=maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            resul+= matriz[l][c]
for c in range(0,3):
    if c == 0:
        maior = menor = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
    elif matriz[1][c] < menor:
        menor = matriz[1][c]
print(f'A soma de todo os valores pares  é igual a: {resul}.')
print(f'A soma dos valores da terceira coluna: {matriz[0][2]+matriz[1][2]+matriz[2][2]}.')
print(f'O menor valor da segunda linha é {menor} e o maior {maior}')