inf = dict()
nome = alt = idade = sexo = 0
while True:
    nome = str(input('NOME:'))
    sexo = str(input('SEXO:[M/F]'))
    while True:
        if sexo in 'mMfF':
            break
        elif sexo != 'mM' or sexo != 'fF':
            print('errado')
            sexo=str(input('SEXO:[M/F]'))
    idade = int(input('Idade:'))
    while True:
        alt = str(input('Quer continuar? [S/N]'))
        if alt in 'nNsS':
            break
        elif alt != 'nNsS':
            print('Errado')
    inf["nome"].append(nome)
    inf["sexo"].append(sexo)
    inf['idade'].append()
    if alt in 'nN':
        break
print(f"{inf}")



