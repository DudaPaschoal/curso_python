##Encapsulamento é um dos conceitos fundamentais em programacao orientada a objeto.
##Ele descreve a ideia de agrupar dados e os métodos que manipulma esses dados em uma unidade.
##Isso impoe restricoes ao acesso direto a variáveis e métodos e pode evitar a modificacao acidental de dados. 
##Para evitar alteracoes acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.


#Inicialização (método __init__):
#nro_agencia: Atributo público para armazenar o número da agência.
#_saldo: Atributo privado para armazenar o saldo, inicializado com 0 por padrão, a menos que especificado.
class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia


#Depositar (método depositar):
#Adiciona o valor do depósito ao saldo atual.
    def depositar(self, valor):
        # ...
        self._saldo += valor


#Sacar (método sacar):
#Verifica se o valor do saque é menor ou igual ao saldo atual antes de subtrair.
#Lança um erro ValueError se o valor do saque exceder o saldo atual.
    def sacar(self, valor):
        # ...
        self._saldo -= valor


#Mostrar Saldo (método mostrar_saldo):
#Retorna o saldo atual.
    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())


##Modificadores de acesso em python nao temos palavras reservadas, porém utilizamos convencoes no nome do recurso, para definir se a variável é pública ou privada.
#Público: Pode ser acessado de fora da classe.
#Privado: Só pode ser acessado pela classe. 

#Propriedades com o property() voce pode criar atributos gerenciados em suas classe. Pode usar atributos gerenciados, tambem conhecidos como propriedades
##Quando precisar modificar sua implementacao interna sem alterar a API pública da classe

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)


#Propriedades Pessoa 

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")