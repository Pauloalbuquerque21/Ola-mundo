listagem = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Trasferidor',4.20,
             'Compasso',9.99,
            'Mochila',120.32,
            'caneta', 22.30,
            'Livro',34.90)   
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    if pos % 2 != 0:
        print(f'R$ {listagem[pos]:7.2f}')