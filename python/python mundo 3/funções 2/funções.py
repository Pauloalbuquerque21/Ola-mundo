#def contador(i,f,p):
#    c=1
#    while c <= f:
#        print(f'{c}',end='..')
#        c += p
#    print('FIM!')

#def soma(a=0,b=0,c=0):
#    """
#    ->
#    a: uma variavel
#    b: 

#    """
#    s = a + b + c
#    print(f'A soma vale {s}')

#soma(4,5,5)




#def teste():
#    x = 8
#    print(f'Na função teste, n vale {n}')
#    print(f'Na função teste, x vale {x}')

#programa pricipal
#n = 2 
#print(f'No programa principal, n vale {n}')
#teste()
#print(f'No programa principal, x vale {x}')

def somar(a=0,b=0,c=0):
    s = a + b + c 
    return s
r1 = somar(3,4,5)
r2 = somar(3,8,9)
r3 = somar(4,7,8)

print(f'Os resultados foram {r1}, {r2} e {r3} ')
