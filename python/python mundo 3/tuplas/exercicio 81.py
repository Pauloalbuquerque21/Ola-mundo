lista = list()
while True:
    lista.append(int(input('Digite um valor:')))
    n1 = str(input('Deseja continuar [S/N]:'))
    if n1 in 'Nn':
        break
print(f'Foi digitado {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores digitados são {lista}')
if lista.count(5) == 0:
    print('Não foi digitado 5.')
else:
    print(f'Foi digitado {lista.count(5)} vezes o valor 5')
