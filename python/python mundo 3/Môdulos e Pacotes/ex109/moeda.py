def metade(met = 0,b=False):
    result = 0
    result = met/2
    return result if b is False else moeda(result)
def dobro(dob = 0,b=False ):
    resultdobro = 0
    resultdobro = dob * 2
    return resultdobro if resultdobro is False else moeda(resultdobro)
def aumentar(aum = 0,b = False):
    resultaum = 0
    porcento = 0
    porcento = (10*aum)/100
    resultaum = aum + porcento
    return resultaum if resultaum is False else moeda(resultaum)
def reduzindo(red = 0,b=False):
    resultreduz = 0 
    porcento = 0
    porcento = (13*red)/100
    resultreduz = red + porcento
    return resultreduz if resultreduz is False else moeda(resultreduz)

def moeda(preço = 0, moeda ='R$'):
    return f'{moeda}{preço:8.2f}'.replace('.',',')