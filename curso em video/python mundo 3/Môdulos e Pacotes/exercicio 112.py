from ex112.utildadescev.moeda import moeda
from ex112.utildadescev.dados import dados
p = dados.leiaDinheiro('Digite o preço:R$')
aum = float(input('Quanto de aumento, em porcentagem:'))
red = float(input('Quanto de redução, em porcentagem:'))
moeda.resumo(p,aum,red)