inf = dict()
inf2 = list()
nome = alt = idade = sexo = result = 0
while True:
    nome = str(input('NOME:'))
    sexo = str(input('SEXO:[M/F]')).upper()
    while True:
        if sexo in 'mMfF':
            break
        elif sexo != 'mM' or sexo != 'fF':
            print('errado')
            sexo=str(input('SEXO:[M/F]')).upper()
    idade = int(input('Idade:'))
    while True:
        alt = str(input('Quer continuar? [S/N]'))
        if alt in 'nNsS':
            break
        elif alt != 'nNsS':
            print('Errado')
    inf["nome"]=nome
    inf["sexo"]=sexo
    inf['idade']=idade
    inf2.append(inf.copy())
    inf.clear()
    if alt in 'nN':
        break
print('-='*30)
for y in range(0,len(inf2)):
    for c in inf2[y][]:
        result = c + result
print(f'A) Ao todo temos {len(inf2)} pessoas cadastradas.')
print(f'B) A média de idade é de {result} anos.')



