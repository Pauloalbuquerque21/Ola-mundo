def le_produto():
    lista_produtos = []
    while True:
        linha = input().strip()
        if linha == '':
            break
        produto = tuple(linha.split('#'))
        produto = (produto[0], produto[1], int(produto[2]), float(produto[3]))
        lista_produtos.append(produto)
    return lista_produtos

def encontra_produto(lista_produtos, codigo_produto):
    for i in range(len(lista_produtos)):
        if codigo_produto == lista_produtos[i][0]:
            return lista_produtos[i]
    return None

def main():
    lista_produtos = le_produto()
    while True:
        codigo_produto = input().strip()
        if codigo_produto == '':
            break
        produto = encontra_produto(lista_produtos, codigo_produto)
        if produto == None:
            print(f"Código {codigo_produto} não localizado na lista de produtos!!!")
        else:
            print("Produto localizado:", produto)
    print("Obrigado por utilizar nosso sistema!!!")

if __name__ == '__main__':
    main()
