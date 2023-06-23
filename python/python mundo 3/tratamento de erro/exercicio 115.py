while True:

    try:
        print('-'*20)
        print('MENU PRINCIPAL')
        print('-'*20)
        print('1 - ver pessoas cadastrada\n2 - Cadastrar nova pessoa\n3 - Sair do Sistema')
        inf = int(input('Sua opção:'))
    except ValueError:
        print('Favor um número válido ')
    if inf != 1 or inf != 2 or inf != 3:
        print('Digite uma opção válida')
    if inf == 3:
        break