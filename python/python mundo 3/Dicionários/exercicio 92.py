inf = dict()
inf['name'] = str(input('Nome:'))
inf['nascimento'] = int(input('Ano do Nascimento:'))
inf['ctps'] = int(input('Carteira de tRABALHO (0 não tem):'))
if inf['ctps'] != 0:
    inf['contratação'] = int(input('Ano de contratação:'))
    inf['salario'] = int(input('Salário: R$'))
print('-='*30)
print(f'- Nome tem o valor {inf["name"]} ')
print(f'- Idade tem o valor {2023-inf["nascimento"]}')
print(f'-ctps tem o valor {inf["ctps"]}')
print(f'-Contratação tem o valor {inf["salario"]}')
print(f'-Aposentadoria tem o valor: {(inf["contratação"]-inf["nascimento"])+35}')