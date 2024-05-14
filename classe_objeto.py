#Classe define as características e comportamentos de um objeto, porém nao conseguimos usá-las diretamente.
#Objetos podem usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

#Exemplo: 
#Classe
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AuAu")

    def dormir(self):
        self.acordado = False
        print("ZZZZzzzz...")

    
#Objeto

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladin", "preto e branco")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)