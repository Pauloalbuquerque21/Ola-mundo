numero = 0
while True:
    numero = int(input('Digite um número:')).strip()
    numero = numero + numero
    if numero == 0:
        print('Numero invalido')
        break