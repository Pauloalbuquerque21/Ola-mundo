from time import sleep
#import random
#n1 = int(input('Teste 1:'))
#n2 = int(input('Teste 2:'))
#n3 = int(input('Teste 3:'))
#n4 = int(input('Teste 4:'))
#lista=[n1,n2,n3,n4]
#random.shuffle(lista)
#n5 = n1 + n2 + n3 + n4
#print('O número da escola é \n{}'.format(lista))
#print(lista)
print('{:=^40}'.format('Tabulada'))
nome=str(input('Qual o seu nome?')).strip()
resposta=str(input('Ola {}, pode me responder algumas perguntas?'.format(nome))).strip().lower()
if resposta == "sim" or  resposta == "s":
    n1 = float(input('Digite um valor:'))
    n2 = float(input('Digite outro valor '))
    soma = n1 + n2
    mult = n1 * n2
    div = n1 / n2
    rest = n1 // n2
    pont = n1 ** n2
    print('Soma:{}\nMultiplicação:{}\nDivisão:{}\nResto da divisão:{}\nPontenciação{}'.format(soma,mult,div,rest,pont))
else:
    print('ok, obrigado')
    sleep(1)
