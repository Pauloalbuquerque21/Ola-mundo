dados = list()
jogador = str(input('Nome do jogador:'))
gols = str(input('Número de GOls:'))


def jog(a=0):
    infjog = 0
    if a == 0:
        infjog ='<Desconhecido>'
    else:
        infjog = a
    return infjog
def gol(b=0):
    infgol = 0 
    if b == 0:
        infgol = 0
    else:
        infgol = b
    return infgol


dados.append(jog(jogador))
dados.append(gol(gols))
print(f'{dados}')


    
