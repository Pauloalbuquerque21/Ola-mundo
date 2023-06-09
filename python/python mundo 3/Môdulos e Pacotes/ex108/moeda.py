def metade(a = 0):
    result = 0
    result = a/2
    return result
def dobro(b = 0):
    resultdobro = 0
    resultdobro = b * 2
    return resultdobro
def aumentar(c = 0):
    resultaum = 0
    porcento = 0
    porcento = (10*c)/100
    resultaum = c + porcento
    return resultaum
def reduzindo(d = 0):
    resultreduz = 0 
    porcento = 0
    porcento = (13*d)/100
    resultreduz = d + porcento
    return resultreduz

def moeda(preço = 0, moeda ='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')



    