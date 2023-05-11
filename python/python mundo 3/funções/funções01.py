def mostralinha():
    print('-------------------')

mostralinha()
print('Sistema de alunos')
mostralinha()
mostralinha()
print(' cadastro de funções')

def mensagem(msg):
    print('--------------')
    print(msg)
    print('--------------')

mensagem('escola')
mensagem('madeira')
mensagem('Escola')

#def soma(res1,res2):
#    print(res1 + res2)
def soma(a,b):
    print(f'A={a} e B={b}')
    s=a+b
    print(s)

soma(2,3)

soma(4,5)

soma(b=3,a=6)

def contador(*num):
    tam =len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)