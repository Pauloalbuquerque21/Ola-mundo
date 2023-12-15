inf = {}
n1 = str(input('Nome:'))
inf['name'] = n1
inf['media']=float(input(f'Média de {n1}:'))
for k, v in  inf.items():
    print(f'{k} é igual a {v}')
#print(f'Nome é igual a {n1}')
#print(f'Média é igual a {inf["media"]}')
if inf["media"] >= 6:
    print('situação do aluno é aprovado')
else:
    print('Situação do aluno é reprovado')