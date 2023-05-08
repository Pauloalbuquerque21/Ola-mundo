inf=dict()
inf2=[]
resul = 0
inf["nome"] = str(input('Nome do jogador:'))
quant = int(input(f'Quantas partidas {inf["nome"]} jogou?'))
for c in range(0,quant):
    inf2.append(int(input(f'  Quantos gols na partida {c}?')))
inf['gols'] = inf2[:]
inf2.clear()
for c in range(0,quant):
    resul = inf['gols'][c]+resul
inf['Total'] = resul
print('-='*30)
print(f'{inf}')
print('-='*30)
print(f'O campo nome tem o valor {inf["nome"]}')
print(f'O campo gols tem o valor {inf["gols"]}')
print(f'O campo total tem o valor {inf["Total"]}')
print(f'-='*30)
print(f'O jogador {inf["nome"]} jogou 5 partidas.')
for c in range(0,quant):
    print(f'=> Na partida {c}, fez {inf["gols"][c]} gols.')
print(f'Foi um Total de {inf["Total"]} gols')
