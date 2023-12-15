expr = input('Digite uma expressão')
abert = []
fech = []
for c in expr:
    if c == '(':
        abert.append(c)
    elif c == ')':
        fech.append(c)
if len(abert) == len(fech):
    print('expressão correta')
else:
    print('Expressão errada')