resultado = list()
dados=list()
total = 0
maior = 0 
menor = 0 
while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    resultado.append(dados[:])
    dados.clear()
    total+=1
    contin = str(input('Deseja continuar [S/N]:'))
    if contin in 'Nn':
        break
for c in resultado:
    if c[1] > maior:
        c = maior
    if c[1] < menor:
        c = menor
print('=-'*30)
print(f'Ao todo, você cadastrou {total} pessoas')
print(f'O maior peso foi de {maior}. Peso de ')
print(f'Valor menor {menor}')


