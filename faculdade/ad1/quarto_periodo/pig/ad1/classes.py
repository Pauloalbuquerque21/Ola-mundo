class suduko():
    def __init__(self,difficult):
        self.difficult = difficult

    def __str__(self):
        return f'{self.difficult}'
    
    def detect(self):
            result = 0
            if len(self.difficult) == len('facil'):#detectar se é facil
                quant = 0
                for letra1, letra2 in zip(self.difficult,'facil'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 5:
                    result = 1
            if len(self.difficult) == len('medio'):#detectar se é medio
                quant = 0
                for letra1, letra2 in zip(self.difficult,'medio'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 5:
                    result = 2
            if len(self.difficult) == len('dificil'):#detectar se é difícil
                quant = 0
                for letra1, letra2 in zip(self.difficult,'dificil'):
                    if letra1 == letra2 :
                         quant +=1
                if quant == 7:
                    result = 3
                      
            return result        

