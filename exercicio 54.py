soma = 0
soma2 = 0
for c in range(1,8):
    n1 = int(input(f'Em que ano a {c} pessoa nasceu:'))
    if 2022-n1 > 18:
        soma=soma+1
    if 2022-n1 < 18:
        soma2=soma2+1
print(f'Tem {soma} pessoas maior de idade')
print(f'Tem {soma2} pessoas menor de idade')
