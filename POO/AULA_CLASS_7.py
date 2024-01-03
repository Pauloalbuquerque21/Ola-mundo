from AULA7 import Escritor
from AULA7 import Caneta
from AULA7 import MaquinaDeEscrever

p1 = Escritor('Paulo')
p2 = Caneta('bic')
maquina = MaquinaDeEscrever()

p1.ferramenta = p2
p1.ferramenta.escrever()