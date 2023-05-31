#n1 = int(input('Em que ano você Nasceu? '))
#def idade(a):
#    b = 2023
#    idade2 = b - a
#    return idade2

#def cat(b):
#    if b >= 65 or b < 16:
#        print('Não é obrigatório')
#    elif 16 < b < 65:
#        print('O votor é obrigatório')

#inf = idade(n1)
#print(f'Com {inf} anos:')
#cat(inf)

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
# Programa principal
nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))
