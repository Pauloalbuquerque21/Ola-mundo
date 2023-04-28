matriz =[[],[],[],[],[],[],[],[],[]]
for c in range(0,9):
    matriz[c].append(int(input(f'Digite um valor para:')))
print('=-'*30)
for c in range(0,3):
    print(f'{matriz[c]}', end='')
print('\n')
for c in range(3,6):
    print(f'{matriz[c]}', end='')
print('\n')
for c in range(6,9):
    print(f'{matriz[c]}', end='')
print('=-'*30)