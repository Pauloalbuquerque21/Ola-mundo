entrada = 0
while True:
    entrada = int(input('Digite um valor entre 0 e 20:'))
    if 20 >= entrada >= 0:
        if entrada == 11:
            break
        else:
            a = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete','Dezoito','Dezenove','Vinte')
            print(f'O valor digitado é {a[entrada]}')
    else:
        print('Numero invalido, tente novamente.')