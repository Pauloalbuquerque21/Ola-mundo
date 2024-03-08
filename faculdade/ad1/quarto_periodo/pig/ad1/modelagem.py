lista = ['.', '.']
resultado = ' '.join(lista)
print(resultado)
for c in range(len(lista)):
    if isinstance(lista[c],str):
        print('sim')
    else:
        print('não')