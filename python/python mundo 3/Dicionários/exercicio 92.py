inf = dict()
inf['name'] = str(input('Nome:'))
inf['nascimento'] = int(input('Ano do Nascimento:'))
inf['ctps'] = int(input('Carteira de tRABALHO (0 não tem):'))
if inf['ctps'] != 0:
    inf['contratação'] = int(input('Ano de contratação:'))
    inf['Salario'] = int(input('Salário: R$'))
print('-='*30)
print(f'-{inf[""]} tem o valor  ')

print(inf)