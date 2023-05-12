list=[]
for c in range(0,3):
    list.append(str(input('Digite uma palabra ou frase: ')))

def resultado(a):
    print('~'*len(a))
    print(f'{a}')
    print('~'*len(a))

for c in range(0,3):
    resultado(list[c])
print(list[1])