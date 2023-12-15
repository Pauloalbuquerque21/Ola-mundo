from time import sleep
import random
list = ('PEDRA','PAPEL','TESOURA')
list2 = (0,1,2)
n2 = random.choice(list2)
n1 = int(input('Suas opções:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nQual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-'*20)
print(f'O jogador escolheu {list[n1]}')
print(f'A maquina escolheu {list[n2]}')
print('-=-'*20)
if n2 == 0:
    if n1 == 0:
        print('Empate')
    elif n1 == 1:
        print('O jogador ganhou')
    elif n1 == 2:
        print('A maquina ganhou')
if n2 == 1:
    if n1 == 0:
        print('A maquina ganhou')
    elif n1 == 1:
        print('Empate')
    elif n1 == 2:
        print('O jogador ganhou')
if n2 == 2:
    if n1 == 0:
        print('O jogador ganhou')
    elif n1 == 1:
        print('A maquina ganhou')
    elif n1 == 2:
        print('Empate')
print('-=-'*20)















#print('Suas opções:')
#print('[0]PEDRA\n[1]PAPEL\n[2]TESOURA')
#n1=int(input('Qual é a sua jagada?'))
#print('JO')
#sleep(1)
#print('KEN')
#sleep(1)
#print('PO!!!')
#sleep(1)
#list=[0,1,2]
#n2 = random.choice(list)
#print('-=-'*20)
#if n2 == 0:
#    print('O computador jogou PEDRA')
#if n2 == 1:
#    print('O computador jogou PAPEL')
#if n2 == 2:
#    print('O computador jogou TESOURA')
#if n1 == 0:
#    print('O jogador escolheu PEDRA')
#if n1 == 1:
#    print('O jogador escolheu PAPEL')
#if n1 == 2:
#    print('O jogador escolheu TESOURA')
#print('-=-'*20)
#if n2 == 0 and n1 == 2 or n2 == 1 and n1 == 0 or n2 == 2 and n2 == 1:
#    print('Jogador perdeu')
#else:
#    print('jogador ganhou')
#if n2 == n1:
#    print('Empate')

