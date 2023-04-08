n1 = int(input('Qual o Valor da casa:'))
n2 = int(input('Qual o seu salário:'))
n3 = int(input('Quantos anos você pensa em pagar:'))
n4=(n1/n3)/12
n5 = (n2*30)/100
if n4 <= n5:
    print('podemos conseder esse emprestimo')
    print(f'30% do salario {n5},Parcela {n4:.2f}')
else:
    print('Não podemos te conseder esse emprestimo.')
    print(f'30% do salario {n5},Parcela {n4:.2f}')

#print(f'{n1},{n2},{n3},{n4:.2f}')