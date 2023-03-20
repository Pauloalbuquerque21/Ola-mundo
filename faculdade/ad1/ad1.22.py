def le_produto():
    """
    Lê da entrada padrão as informações de um produto e retorna um dicionário com essas informações.
    """
    linha = input().strip()
    if linha == "":
        return None
    codigo, descricao, quantidade, preco = linha.split("#")
    produto = {"codigo": codigo, "descricao": descricao, "quantidade": int(quantidade), "preco": float(preco)}
    return produto

def busca_produto(codigo, lista_produtos):
    """
    Busca um produto na lista de produtos pelo seu código.
    Retorna o dicionário com as informações do produto, caso seja encontrado, ou None, caso contrário.
    """
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

def main():
    # Lê a lista de produtos
    lista_produtos = []
    while True:
        produto = le_produto()
        if produto is None:
            break
        lista_produtos.append(produto)

    # Busca de produtos
    while True:
        codigo = input("Digite o código do produto (ou vazio para sair): ").strip()
        if codigo == "":
            break
        produto = busca_produto(codigo, lista_produtos)
        if produto is None:
            print("Produto não encontrado!")
        else:
            print("Código:", produto["codigo"])
            print("Descrição:", produto["descricao"])
            print("Quantidade:", produto["quantidade"])
            print("Preço:", produto["preco"])

    print("Obrigado por utilizar nosso sistema!!!")

if __name__ == "__main__":
    main()