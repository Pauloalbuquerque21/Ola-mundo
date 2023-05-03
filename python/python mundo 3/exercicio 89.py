inf=[]
ind=[]
name=0
nota1=nota2=0
while True:
    ind.append(input('Digite seu nome:'))
    ind.append(float(input('Nota 1:')))
    ind.append(float(input('Nota 2:')))
    ater= str(input('Quer continuar? [S/N]'))

    if ater in 'nN':
        break
