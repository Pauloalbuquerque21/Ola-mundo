n1 = int(input('Digite um número \npara calcular seu fatorial:'))
n2 = n1
c= n2
f=1
while c > 0:
    print(c,end=" ")
    print('x'if c>1 else "=",end=" ")
    f*=c
    c-=1
print(f)