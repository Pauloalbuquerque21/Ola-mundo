palavras = ('APRENDENR','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
n1 = 0 
for pos in palavras:
    print(f'\nNa palavra {pos} temos',end=' ')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')