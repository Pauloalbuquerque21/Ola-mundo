n1 = int(input('Em que ano você Nasceu? '))
def idade(a):
    b = 2023
    idade2 = b - a
    return idade2

def cat(b):
    if b >= 65 or b < 16:
        print('Não é obrigatório')
    elif 16 < b < 65:
        print('O votor é obrigatório')

inf = idade(n1)
print(f'Com {inf} anos:')
cat(inf)
