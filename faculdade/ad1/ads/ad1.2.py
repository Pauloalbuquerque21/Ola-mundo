def preencher_vetor(n):
    pessoas = []
    for i in range(n):
        nome = str(input("Digite o nome da pessoa: "))
        idade = int(input("Digite a idade da pessoa: "))
        peso = float(input("Digite o peso da pessoa: "))
        altura = float(input("Digite a altura da pessoa: "))
        pessoas.append((nome, idade, peso, altura))
    return pessoas

def imprimir_dados_pessoas(pessoas, informacao):
    if informacao == 0:
        
        primeira_pessoa = pessoas[0]
        print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*primeira_pessoa))
        for pessoa in pessoas:
            if pessoa[0] > primeira_pessoa[0]:
                print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*pessoa))
    elif informacao == 1:
        primeira_pessoa = pessoas[0]
        print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*primeira_pessoa))
        for pessoa in pessoas:
            if pessoa[1] > primeira_pessoa[1]:
                print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*pessoa))
    elif informacao == 2:
        primeira_pessoa = pessoas[0]
        print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*primeira_pessoa))
        for pessoa in pessoas:
            if pessoa[2] > primeira_pessoa[2]:
                print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*pessoa))
    elif informacao == 3:
        primeira_pessoa = pessoas[0]
        print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*primeira_pessoa))
        for pessoa in pessoas:
            if pessoa[3] > primeira_pessoa[3]:
                print("Nome: {}\nIdade: {}\nPeso: {}\nAltura: {}\n".format(*pessoa))
    else:
        print("Opção inválida!")
print("Bem-vindo ao programa de cadastro de pessoas!")
n = int(input("Digite a quantidade de pessoas a serem cadastradas: "))
pessoas = preencher_vetor(n)
informacao = int(input("Digite a informação desejada (0-nome, 1-idade, 2-peso, 3-altura): "))
imprimir_dados_pessoas(pessoas, informacao)
print("Obrigado por utilizar nosso sistema!!!")