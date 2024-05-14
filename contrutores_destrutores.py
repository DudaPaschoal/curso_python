#Método Construtor sempre é executada quando uma nova instancia da classe é criada. Nesse método inicializamos o estado do nosso objeto. 
#Para declarar o método construtor da classe, criamos um método com o nome __init__.

    #__init__. 
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

#Destrutor sempre é executado quando uma instancia(Objeto) é destruida. Destrutores em python nao sao tao necessários quanto em C++ porque o python tem um coletor de lixo que lida 
#com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe criamos um método com o nome __del__. 

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()