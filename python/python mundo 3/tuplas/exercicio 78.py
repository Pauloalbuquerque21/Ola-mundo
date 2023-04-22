valores = list()
mai = 0
men = 0 
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {c}:')))
    if c == 0:
        man = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posições', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')

#vezes = 0

#for c in range(0,5):
#    valores.append(int(input(f'Digite um valor para a posição {vezes}:')))
#    vezes= vezes + 1
#print(f'Você digitou os valores {valores}')
#if valores.count(max(valores)) > 1:
#    print(f'O maior valor digitado foi {max(valores)} nas posições #{valores.index(max(valores))}')
#else:
#    print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}') 
#if valores.count(min(valores)) > 1:
#    print(f'O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))}')
#else:
#    print(f'O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))} ')