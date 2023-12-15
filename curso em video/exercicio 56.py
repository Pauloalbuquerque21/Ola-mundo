soma = soma2=maior=0
for c in range(1,5):
    print(f'-----{c} PESSOA-----')
    n1 = str(input('Nome:'))
    n2 = int(input('Idade:'))
    n3 = str(input('Sexo [M/F]:')).lower()
    soma = soma+n2
    if n3 == 'f' and n2<20:
        soma2 = soma2 + 1
    if n2>maior:
        maior =n2
        nome = n1
n4=soma/4
print(f'{soma}')
print(f'A média de idade do grupo é de {n4:.2f} anos')
print(f'Ao todo são {soma2} mulheres com menos de 20 anos')
print(f'Idade maior{maior} é a pessoa {nome}')

print('teste')
