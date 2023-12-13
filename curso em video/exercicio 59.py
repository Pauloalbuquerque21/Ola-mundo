n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = 0
n4 = n1+n2
n5 = n1*n2
while n3 != 5:
    n3 = int(input(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números:\n [5] Sair do programa\n>>>>>Qual é a sua opção?'))
    if n3 == 1:
        print('-=-'*20)
        print(f'A soma de {n1} e {n2} é igual {n4}')
        print('-=-'*20)
    elif n3 == 2:
        print('-=-'*20)
        print(f'A multiplicação de {n1} e {n2} é igual {n5} ')
        print('-=-'*20)
    elif n3 == 3:
        if n1 > n2 :
            maior = n1
        elif n1 < n2:
            maior = n2
        print(f'O primeiro número é {n1} e segundo {n2} o maior é {maior}')
    elif n3 == 4:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
    elif n3 == 5:
        print('Finalizando.....')




