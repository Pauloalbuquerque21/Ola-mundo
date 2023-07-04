from ex115.opções import opções
from ex115.arquivo import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)
while True:  
    resposta = opções.menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do sistema'])
    if resposta == 1:
        #c
        arquivo.lerArquivo('Opção 1')
    elif resposta == 2:
        opções.cabeçalho('Opção 2')
    elif resposta == 3:
        opções.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida')
    sleep(2) 