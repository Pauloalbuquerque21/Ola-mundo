from classes import suduko
print('-+'*20)
print(f'SUDOKO'.center(20))
print('-+'*20)

dificuldade = suduko(str(input('Digite a Dificuldade[Facil,Medio e Dificil]').strip().lower()))
print(dificuldade)

print(dificuldade.detect())


