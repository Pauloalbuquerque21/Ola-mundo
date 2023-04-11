#Funções

#funções sem argumento
#def mensagem():
#    print('mensagem')

#mensagem()

#Função com argumento simples
#x = 10
#y = 20

#def soma (a,b):
#    return a + b

#r = soma(x , y)
#print(r)
#print(f'A soma entra {x} e {y} é igual {r}')

#Função mais complexa

valores = [1,2,3,4,5]
def quadrado(valores):
    quadrados = []
    for x in valores:
        quadrados.append(x**2)
    return quadrados
    
resultados = quadrado(valores)

for y in resultados:
    print(y)