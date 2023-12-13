lista = []
impar = []
par = []
while True:
    lista.append(int(input('Digite um número:')))
    opc = input('Quer continuar? [S/N]')
    
#    if valores % 2 == 0:
#        par.append(valores)
#    if valores % 2 != 0:
#        impar.append(valores)
    if opc in 'Nn':
        break
for i , v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
     
print(f'Os números digitados foram {lista}')
print(f'Os números impares digitados foram {impar}')
print(f'Os números pares digitados foram {par}')

