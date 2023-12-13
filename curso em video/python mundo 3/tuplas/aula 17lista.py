#lanche = [1,2,3,4]
#lanche[0] = 4
#print(lanche)
#lanche.pop(3)
#lanche.remove(4)
#del lanche[0]
#print(lanche)
#if 1 in lanche:
#    lanche.remove(1)
#else:
#    lanche.append(1)
#print(lanche)
#num = [2,5,9,1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2,0)
#num.pop(2)
#print(num)
#print(f'A quantidade de elementos dessa lista {len(num)}')
#valores = list()
#for c in range(0,5):
#    valores.append(int(input('Digite um valor:')))
#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}')
#print('Cheguei ao final da listagem.')
a = [2,3,4,7]
b = a[:]
b[2]=8
print(f'Lista A:{a}')
print(f'Lista B:{b}')