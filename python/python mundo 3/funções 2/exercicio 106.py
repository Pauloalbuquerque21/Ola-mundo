def ajuda(a):
    help(a)
n1 = ''
while True:
    n1 = str(input('Função ou Biblioteca >')).strip().lower()
    if n1 == 'fim':
        break
    else:
        ajuda(n1)


