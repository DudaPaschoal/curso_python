#Interfaces definem o que uma classe devem fazer e nao como. 
#O conceito de interface é definir um contrato, onde sao declarados os métodos (o que deve ser feito) e suas respectivas assinaturas.
#Em python utilizamos classes abstratas para criar contratos. Classes abstratas nao podem ser instanciadas. 

#Explicação do Código
#Classe Abstrata ControleRemoto:

#A classe ControleRemoto é uma classe abstrata (derivada de ABC - Abstract Base Class).
#Contém métodos abstratos ligar e desligar que devem ser implementados por qualquer classe derivada.
#Também possui uma propriedade abstrata marca, que deve ser implementada como uma propriedade em subclasses.
#Classe ControleTV:

#Herda de ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca.
#Os métodos ligar e desligar fornecem a lógica específica para ligar e desligar a TV.
#A propriedade marca retorna a marca da TV, neste caso "Philco".
#Classe ControleArCondicionado:

#Herda de ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca.
#Os métodos ligar e desligar fornecem a lógica específica para ligar e desligar o ar condicionado.
#A propriedade marca retorna a marca do ar condicionado, neste caso "LG".


from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)



#Criação e Uso de ControleTV:

#controle = ControleTV(): Cria uma instância de ControleTV.
#controle.ligar(): Liga a TV, imprimindo "Ligando a TV..." seguido de "Ligada!".
#controle.desligar(): Desliga a TV, imprimindo "Desligando a TV..." seguido de "Desligada!".
#print(controle.marca): Imprime a marca da TV, "Philco".
#Criação e Uso de ControleArCondicionado:

#controle = ControleArCondicionado(): Cria uma instância de ControleArCondicionado.
#controle.ligar(): Liga o ar condicionado, imprimindo "Ligando o Ar Condicionado..." seguido de "Ligado!".
#controle.desligar(): Desliga o ar condicionado, imprimindo "Desligando o Ar Condicionado..." seguido de "Desligado!".
#print(controle.marca): Imprime a marca do ar condicionado, "LG".
#Conclusão
#Este código demonstra como usar classes abstratas e herança para criar uma estrutura comum para diferentes tipos de controles remotos. 
#A classe abstrata ControleRemoto define a interface que todas as subclasses devem implementar, garantindo que cada controle remoto tenha métodos ligar e desligar 
#e uma propriedade marca. As classes ControleTV e ControleArCondicionado implementam essa interface de maneiras específicas, 
#proporcionando a funcionalidade necessária para cada tipo de dispositivo.