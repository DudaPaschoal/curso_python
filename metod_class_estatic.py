
##Métodos de classe estao ligados a classe e nao ao objeto. Eles tem acesso ao estado da classe, pois recebem um parametro que aponta para a classe e nao para a instancia do objeto. 
##Métodos estáticos nao recebe um primeiro argumento explícito. Ele também é um método vinculado á classe e nao ao objeto da classe. Esse metodo nao pode acessar ou modificar o estado
#da classe. Ele está presente em uma classe porque faz sentido que o metodo esteja presente na classe.



#Vamos analisar a classe Pessoa que você forneceu. Esta classe possui um método de classe (classmethod) e um método estático (staticmethod), além do método construtor (__init__).

#Explicação do Código
#Método Construtor (__init__):
#__init__(self, nome, idade): Este método inicializa uma instância da classe Pessoa com os atributos nome e idade.
#Método de Classe (@classmethod):

#@classmethod def criar_de_data_nascimento(cls, ano, mes, dia, nome): Este método permite criar uma instância da classe Pessoa a partir da data de nascimento.
#Calcula a idade subtraindo o ano de nascimento do ano atual (2022, neste caso).
#Retorna uma nova instância da classe Pessoa usando cls(nome, idade).
#Método Estático (@staticmethod):

#@staticmethod def e_maior_idade(idade): Este método verifica se a idade fornecida é maior ou igual a 18 anos.
#Retorna True se a idade for maior ou igual a 18, caso contrário, retorna False.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade, Pessoa.e_maior_idade(p.idade))

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

#Criação de Instância com criar_de_data_nascimento:

#p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme"): Cria uma nova instância da classe Pessoa calculando a idade com base no ano de nascimento (1994). A idade calculada será 2022 - 1994 = 28.
#print(p.nome, p.idade): Imprime o nome e a idade da pessoa. Saída: Guilherme 28.
#Verificação de Maioridade com e_maior_idade:

#print(Pessoa.e_maior_idade(18)): Verifica se 18 anos é maioridade. Saída: True.
#print(Pessoa.e_maior_idade(8)): Verifica se 8 anos é maioridade. Saída: False.

#Este código ilustra o uso de métodos de classe para criar instâncias de uma classe com base em diferentes critérios (neste caso, a data de nascimento) 
#e o uso de métodos estáticos para funções utilitárias que não dependem de instâncias da classe (neste caso, verificar se uma idade corresponde à maioridade). 
#A implementação está correta e os métodos funcionam conforme esperado.