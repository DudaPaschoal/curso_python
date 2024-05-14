
#A biblioteca re é utilizada para trabalhar com expressões regulares em Python.
import re

    #A função verifica se o número de telefone passado como argumento corresponde ao padrão definido.
def validate_numero_telefone(phone_number):

    #A variável padrao contém a expressão regular que define o formato esperado.

    padrao = r"^\(\d{2}\) 9\d{4}-\d{4}$"

    # A função re.match compara a string de entrada com a expressão regular. Se houver correspondência, retorna uma mensagem de número válido, caso contrário, retorna uma mensagem de número inválido.
    if re.match(padrao, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."
    

    #Esta linha solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável phone_number.
phone_number = input()

    #Esta linha chama a função validar_numero_telefone com o número de telefone fornecido pelo usuário como argumento e armazena o resultado na variável result.
result = validate_numero_telefone(phone_number)

    #Esta linha imprime o resultado retornado pela função, indicando se o número de telefone é válido ou inválido.
print(result)