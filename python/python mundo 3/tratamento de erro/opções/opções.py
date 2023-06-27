def inf(a):
    while True:
        print('-'*20)
        print('MENU PRINCIPAL')
        print('-'*20)
        print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do Sistema')
        try:
            n1 = int(input(a))
        except:
            print('Erro!Digite um número inteiro válido')
        else:
            if n1 == 1 or n1 == 2 or n1 == 3:
                if n1 == 3:
                    return n1
                else:
                    print('-'*20)
                    print(f'Opção {n1}')
                    print('-'*20)
            else:
                print('Digite um valor válido')
                