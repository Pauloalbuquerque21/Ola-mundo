soma=0
quant=0
for c in range(1,500,2):
    if c%3 == 0:
        soma=soma+c
        quant=quant+1
print(f'Soma:{soma}\nQuantidade: {quant}')