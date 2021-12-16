print('-=-'*30)
print('Analisador de triangulo')
print('-=-'*30)
n1 = float(input('Primeiro Lado do triangulo:'))
n2 = float(input('Segundo lado do triangulo:'))
n3 = float(input('Terceiro lado do triangulo:'))
if n1+n2>n3 and n2+n3>n1 and n3+n1>n2:
    print('Com essas medidas tem como forma um triangulo.')
else:
    print('com essas medidas não tem como forma um triangulo:')