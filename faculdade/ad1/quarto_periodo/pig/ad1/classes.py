import random
class suduko():
    def __init__(self,difficult):
        self.difficult = difficult
    def __str__(self):
        return f'{self.difficult}'
    
    def suduku_pricipal(self):
        listas=[[],[],[],[],[],[],[],[],[]]
        for c in range(0,9):
            for c2 in range(0,9):
                listas[c].append(".")
        return listas
    
    def suduko_usuario(self,listas,dificuldade):
        erros = 0
        horinzontal = ['0','1','2','3','4','5','6','7','8']
        vertical = [0,1,2,3,4,5,6,7,8]
        etapa = 0
        linha_maquina = 0
        vezes = 0
        valores_coluna = 0

        while True:#loop do jogo
            lista_visual = list()

            if  etapa == 0 :
                if dificuldade == 0 :
                    if valores_coluna == 4:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
                elif dificuldade == 1 :
                    if valores_coluna == 3:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
                elif dificuldade == 2 :
                    if valores_coluna == 2:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
                print(f'Coluna:{coluna}, linha:{linha_maquina}, valor:{valor},valores_coluna:{valores_coluna}')
            else:
                horizontal_visual = ' '.join(horinzontal)

                print(f'   {horizontal_visual}')
                print('  ------------------')
                for c in range(0,9):
                    hozontal_ventical = ' '.join(horinzontal)
                    lista_visual = ' '.join(listas[c])
                    print(f'{vertical[c]}| {lista_visual}')
                linha_usuario = int(input('Digite a linha:'))
                coluna_usuario = int(input('Digite a coluna:'))
                valor_usuario = str(input('digite o valor '))
                linha = linha_usuario
                coluna = coluna_usuario
                valor = valor_usuario


            #veriaveis:
            confere_inferior = 0
            confere_superior = 0
            confere_linha = 0
            quadrado = 0
            # conferir se está na linha:
            if valor not in listas[linha]:
                confere_linha += 1
            #verificar as linhas inferiores, mesma coluna:
            for quant2 in range(linha-1,-1,-1):
                if valor != listas[quant2][coluna]:
                    confere_inferior += 1
            #verificar linhas superiores, da mesma coluna:
            for superior in range(linha+1,9):
                if valor != listas[superior][coluna]:
                    confere_superior += 1
            #verificar os quadrados:
            #quadrado 1        
            if (linha <=2) and (coluna <=2):
                for linha_verif in range(0,3):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            
            #quadrado 2
            elif (linha <= 2) and (3 <= coluna <=5):
                for linha_verif in range(0,3):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 3
            elif (linha <=2) and (6<=coluna <=8):
                for linha_verif in range(0,3):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 4
            elif (3<=linha <=5) and (coluna <=2):
                for linha_verif in range(3,5):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 5
            elif (3<=linha <=5) and (3 <= coluna <=5):
                for linha_verif in range(3,6):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 6
            elif (3<=linha <=5) and (6<=coluna <=8):
                for linha_verif in range(3,6):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 7
            elif (6<=linha <=8) and (coluna <=2):
                for linha_verif in range(6,9):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 8
            elif (6<=linha <=8) and (3 <= coluna <=5):
                for linha_verif in range(6,9):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 9
            elif (6<=linha <=8) and (6<=coluna <=8):
                for linha_verif in range(6,9):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            

            if (confere_inferior == linha) and (confere_superior == (9-(linha+1))) and (confere_linha == 1) and (quadrado == 0):
                print(f'adicionou {valor}')
                listas[linha][coluna] = valor
                if etapa == 0:
                    vezes+=1
                    valores_coluna +=1
                    if dificuldade == 0:
                        if vezes == 36:
                            etapa+=1
                    if dificuldade == 1:
                        if vezes == 27:
                            etapa+=1
                    if dificuldade == 2:
                        if vezes == 18:
                            etapa+=1     
            else:

                print('-------Jogada errada---------')
                if etapa == 1:
                    erros +=1
                    if erros == 4:
                        break




    def detect(self):
            result = 0
            if len(self.difficult) == len('facil'):#detectar se é facil
                quant = 0
                for letra1, letra2 in zip(self.difficult,'facil'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 5:
                    result = 0
            if len(self.difficult) == len('medio'):#detectar se é medio
                quant = 0
                for letra1, letra2 in zip(self.difficult,'medio'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 5:
                    result = 1
            if len(self.difficult) == len('dificil'):#detectar se é difícil
                quant = 0
                for letra1, letra2 in zip(self.difficult,'dificil'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 7:
                    result = 0
                      
            return result        

