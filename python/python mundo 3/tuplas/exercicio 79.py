valores = list()

while True:
    n = int(input('Digite um valor:'))
    if n not in valores:
        valores.append(n)
    print('Valor adicionado com sucesso...')
    n1= str(input('Quer continua?[S/N]')).lower()
    if n1 in 'Nn':
        print('-='*30)
        break
 
print(f'Você Digitou os valores {sorted(valores)}')

