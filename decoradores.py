def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))


#calculador

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))

#PRIMEIRO DECORADOR
#O Python permite que voce use decoradores de maneira mais simples com o simbolo @

def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


ola_mundo()

####


def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("João", 1000)
print(resultado)
print(ola_mundo)


##Iteradores é um objeto que contém um numero contável de valores que podem ser iterados, o que significa que voce poode percorrer todos os valores.
##__iter__ e __next__
##Economizar memória evitando carregar todas as linhas do arquivo
#Iterar linha a linha do arquivo 

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)


    #Geradores sao tipos especiais de iteradores, ao contrario das listas ou outros iteráveis, nao armazenam todos os seus valores na memória.  
    #Sao definidos usando funcoes regulares, mas, ao invés de retornar valores usando "return" utilizam "yield"

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)



    

