def leiaint(a):
    while True:
        try:
            n1 = int(input(a))
        except:
            print('Erro! Digite um valor inteiro válido!')
        else:
            return n1

def leiafloat(a):
    while True:
        try:
            float1 = float(input(a))
        except:
            print('ERRO! Digite um valor real válido!')
        else:
            return float1