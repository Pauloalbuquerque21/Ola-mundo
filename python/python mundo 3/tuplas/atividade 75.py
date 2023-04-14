num = (int(input('Digite um número:')), 
       int(input('Digite outro número:')), 
       int(input('Digite mais um número:')), 
       int(input('Digite o último número:')))
                                           
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'Você digitou {num.count(9)} vezes, o valor 9')
else:
    print(f'Você não digitou o valor 9')
if 3 in num:
    print(f'você digitou valor 3 na {(num.index(3))+1} posição')
else:
    print(f'você não digitou o valor 3')
print(f'Os valores pares são:',end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
