n1 = c = f = 0
while n1 != 999:
    c+=1
    f+=n1
    n1 = int(input('Digite um número:[999 para parar]:'))
print(f'Você digitou {c-1} números e o total é igual a {f}')
