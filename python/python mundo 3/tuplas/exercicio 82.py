lista = []
impar = []
par = []
while True:
    valores = int(input('Digite um número:'))
    opc = input('Quer continuar? [S/N]')
    lista.append(valores)
    if opc in 'Nn':
        break
    else:
        if valores % 2 == 0:
            par.append(valores)
        else:
            impar.append(valores)

print(f'Os números digitados foram {lista}')
print(f'Os números impares digitados foram {impar}')
print(f'Os números pares digitados foram {par}')

