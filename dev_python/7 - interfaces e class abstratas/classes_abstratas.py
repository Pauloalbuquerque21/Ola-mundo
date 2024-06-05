from abc import ABC, abstractmethod, abstractproperty
#class abstrata precisa do modulo abc class ABC

#class principal que filha de ABC

class ControleRemoto(ABC):

    #Usamos esse decorar da definir esse metodo como abstrado, agora cada class que for filho da controle remoto, irá ter que ter esse método
    @abstractmethod
    def ligar(self):
        pass


    @abstractmethod
    def desligar(self):
        pass
    
    #Com esses decoradores, definimos que todos as class que herdarem os métodos de Controle Remoto, terão que definir e ter esse método.
    property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    # podemos personalizar os métodos, porém tem que ter esses métodos, pois dizemos que controle remoto no mínimo tem esses métodos
    def ligar(self):
        print('Ligando a TV ...')
    
    def desligar(self):
        print('Desligando a TV ...')
        print('Desligada!')
    
    def marca(self):
        return "LG"
    

class ControleArCondicionado(ControleRemoto):
    
    
    def ligar(self):
        print('Ligando o Ar condicionado ...')
        print('Ligado!')

    def desligar(self):
        print('Desligando o Ar Condicionado ...')
        print('Desligado!')

    @property
    def marca(self):
        return "LG"

# obs: CLasses abstratas não podem ser instânciadas.
#controle = ControleRemoto()

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()


