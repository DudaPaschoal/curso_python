#Classe Estudante e Função mostrar_valores
#O código define uma classe Estudante que representa um estudante com um nome, uma matrícula e uma escola,
#e uma função mostrar_valores que imprime os valores dos objetos passados como argumento.


#Atributo de Classe:
#escola = "DIO": Este é um atributo de classe, o que significa que é compartilhado por todas as instâncias da classe Estudante.
#Inicialização (__init__):
#def __init__(self, nome, matricula): Método construtor que inicializa os atributos de instância nome e matricula.
class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

#Representação em String (__str__):
#def __str__(self) -> str: Método especial que define a representação em string do objeto. Quando print(obj) é chamado, ele retorna a string formatada com nome, matricula e escola.
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


#Função mostrar_valores:
#def mostrar_valores(*objs): Esta função aceita um número variável de argumentos (*objs) e imprime cada um deles, 
#utilizando a representação em string definida no método __str__ da classe Estudante.
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

#Criação dos Estudantes:
#aluno_1 e aluno_2 são criados com a escola padrão "DIO".
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)


#Alteração do Atributo de Classe:
#Estudante.escola = "Python" altera o atributo de classe escola para "Python". Isso afeta todas as instâncias da classe.
#Criação do Terceiro Estudante:
#aluno_3 é criado com a nova escola "Python".
#Mostrar Valores Novamente:
#mostrar_valores(aluno_1, aluno_2, aluno_3) imprime:
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

#O atributo de classe escola é compartilhado por todas as instâncias de Estudante. Quando ele é alterado, essa mudança se reflete em todas as instâncias, incluindo aquelas já criadas. 
#A função mostrar_valores imprime a representação em string dos objetos Estudante, que inclui o nome, a matrícula e a escola.