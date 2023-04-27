resultado =[]
dados=[]
total = 0
maior = 0 
menor = 0 
while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    if len(dados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    resultado.append(dados[:])
    dados.clear()
    total+=1
    contin = str(input('Deseja continuar [S/N]:'))
    if contin in 'Nn':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {total} pessoas')
print(f'O maior peso foi de {maior}. Peso de ')
print(f'Valor menor {menor}')


