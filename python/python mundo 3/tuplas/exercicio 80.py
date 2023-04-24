valores = list()
for c in range(0,5):
    n1 = int(input('Digite um valor:'))
    if len(valores) == 0:
        valores.append(n1)
        print('Primeiro valor adicionado...')
    else:
        if valores[0] > n1:
            valores.insert(0,n1)
            print('Adicionado na posição 0')
        else:
            if valores[1] > n1 or len(valores)==1:
                valores.insert(1,n1)
                print('Adicionado na posição 1')
            if valores[2] > n1 and len(valores) == 2:
                valores.insert(2,n1)
                print('Adicionado na posição 2')
            if valores[3] > n1 and len(valores)==3:
                valores.insert(3,n1)
                print('Adicionado na posição 3')
            if valores[4] > n1 and len(valores) == 4:
                valores.insert(4,n1)
                print('Adicionado na posição 4')

print(f'Os valores cadastrados são {valores}')