from opções import opções
from time import sleep

while True:
    resposta = opções.menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do sistema'])
    if resposta == 1:
        opções.cabeçalho('Opção 1')
    elif resposta == 2:
        opções.cabeçalho('Opção 2')
    elif resposta == 3:
        opções.cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro! Digite uma opção válida')
    sleep(2)