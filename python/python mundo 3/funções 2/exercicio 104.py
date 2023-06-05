

def leiaInt(a=0):
 
    if len(a) == 0:
        print('ERRO! Digite um número inteiro válido.')
    else:
        a = str(a)
        if a.isnumeric():
            a = int(a)
            print(f'Você digitou o número {a}')
        else:
            print('ERRO! Digite um número inteiro válido.')
        return a
n = leiaInt(input('Digite um número:'))