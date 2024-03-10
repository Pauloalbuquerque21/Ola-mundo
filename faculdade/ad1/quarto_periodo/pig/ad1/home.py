from classes import suduko
print('-+'*20)
print(f'SUDOKO'.center(20))
print('-+'*20)

dificuldade = suduko(str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower()))
print(dificuldade)

lista=dificuldade.suduku_pricipal()

dificuldade.suduko_usuario(lista)

print(dificuldade.detect())


