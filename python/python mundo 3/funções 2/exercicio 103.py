dados = list()
jogador = str(input('Nome do jogador:'))
if len(jogador) == 0:
    dados = '<Desconhecido>'
else:
    dados.append(jogador)
gols = str(input('Número de GOls:'))
dados.append(gols)

print(f'{dados}')

