colocação = ('América-MG','Athletico-PR','Atlético-MG','Bahia','Botafogo','Corinthians','Coritiba','Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Bragantino','Santos','São Paulo','Vasco')
primeiros=int(input('Quais os primeiros colocados que você quer ver de 1 a 20:'))
ultimos=int(input('Quais os ultimos colocados:'))
posição=str(input('Digite seu time:')).strip().capitalize()
print('Os primeiros:')
for c in range(0,primeiros):
   print(colocação[c])
print('Os Últimos:')
for c in range(19,20-(ultimos+1),-1):
    print(colocação[c])
print(sorted(colocação))
print(f'o {posição} está na posição {colocação.index((posição+1))}')