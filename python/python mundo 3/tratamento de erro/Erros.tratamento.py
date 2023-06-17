try:
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    n3 = n1/n2
except Exception as erro:
    print(f'Problema encontrado, foi {erro.__class__}')
except ZeroDivisionError:
    print('')
else:
    print(f'O resultado é {n3}')
finally:
    print('Volte sempre! Muito obrigado!')
