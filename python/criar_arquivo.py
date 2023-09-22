#ler = read

with open('arquivo.txt','r') as arquivo:
    dados = arquivo.read()
print(dados)

with open('arquivo.txt','r',encoding='utf-8') as dado:
    dados_2 = dado.readlines()
print(dados_2)


#escrever = wride 
#modificar e criar um novo arquivo
with open('arquivo.txt','w') as modi:
    modi.write('Estudando modificar arquivo')

#adicionar informação do arquivo
with open('arquivo.txt','a') as adi:
    adi.write('\nagora estudando adicionar arquivos')