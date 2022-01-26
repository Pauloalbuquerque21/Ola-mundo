n1=n2=c=f=0
while n2 != "n":
    n1 = int(input('Digite um número:'))
    n2 = str(input('Quer continuar?[S/N]')).lower()
    c+=1
    f+=n1
n3=f/c
print(f'Você digitou {c} números, e a soma é igual a {f} e a média é igual a {n3:2f}')  