#dados = list()
#jogador = str(input('Nome do jogador:')).strip()
#if len(jogador) == 0:
#    jogador = 0
#gols = str(input('Número de GOls:')).strip()
#if len(gols) == 0:
#    gols = 0
#def jog(a=0):
#    infjog = 0
#    if a == 0:
#        infjog ='<Desconhecido>'
#    else:
#        infjog = a
#    return infjog
#def gol(b=0):
#    infgol = 0 
#    if b == 0:
#        infgol = 0
#    else:
#        infgol = b
#    return infgol
#dados.append(jog(jogador))
#dados.append(gol(gols))


#print(f'O jogador {dados[0]} fez gols(s) no compeonato')

def ficha(jog="Desconhecido", gol = 0):
    print(f'O gadoror {jog} fez {gol} gol(s) no compeonato')

#Programa principal
n = str(input('Nome do jogador:'))
g = str(input('Número de Gols'))

if g.isnumeric():
    g = int(g)
else:
    g = 0 
if n.strip() == "":
    ficha(gol=g)
else:
    ficha(n,g)
    
