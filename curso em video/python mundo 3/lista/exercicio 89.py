inf=[]
ind=[]
name=0
nota1=nota2=0
while True:
    ind.append(input('Digite seu nome:'))
    ind.append(float(input('Nota 1:')))
    ind.append(float(input('Nota 2:')))
    ater= str(input('Quer continuar? [S/N]'))
    inf.append(ind[:])
    ind.clear()
    if ater in 'nN':
        break
print('-'*30)
for c in range(0,len(inf)):
    print(f'{c} {inf[c][0]}  {(inf[c][1]+inf[c][2])/2}')
print('-'*30)

