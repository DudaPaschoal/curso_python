##elaborado

#Importa o módulo textwrap, que é usado para remover indentação comum de blocos de texto.
import textwrap

#Define a função menu que exibe o menu principal do programa.
#menu = """\n...""": Define uma string multilinha que representa o menu.
def menu():
    menu = """\n
================ MENU ================
    [n]\tRecomendar Plano
    [q]\tSair
======================================
    => """

    #Exibe o menu e aguarda a entrada do usuário, retornando a escolha do usuário.
    # Remove a indentação comum do bloco de texto menu para que ele seja exibido corretamente.
    return input(textwrap.dedent(menu))

#def recomendar_plano(consumo, /):: Define a função recomendar_plano que aceita um argumento posicional consumo.
#O / após consumo indica que consumo deve ser um argumento posicional (isso é mais relevante em funções complexas, mas não é necessário aqui).
def recomendar_plano(consumo, /):
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.")
    elif consumo <= 20 and consumo > 10:
        print("Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.")
    elif consumo >= 21: 
        print("Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.")


#def main():: Define a função principal main que contém o loop principal do programa.
#while True:: Inicia um loop infinito que continua até que uma condição de parada seja atendida.
#opcao = menu(): Chama a função menu() para exibir o menu e obtém a escolha do usuário.
def main():
    while True:
        opcao = menu()

        #if opcao == "n":: Verifica se a escolha do usuário é "n", que indica que ele deseja recomendar um plano.
        #consumo = float(input("Informe o consumo médio mensal de Dados:")): Solicita ao usuário que informe o consumo médio mensal de dados e converte a entrada para um número float.
        #recomendar_plano(consumo): Chama a função recomendar_plano com o valor de consumo fornecido pelo usuário.
        if opcao == "n":
            consumo = float(input("Informe o consumo médio mensal de Dados:"))
            recomendar_plano(consumo)
        elif opcao == "q":
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
#main(): Chama a função main para iniciar a execução do programa.
main()


##simples para concluir desafio

#def recomendar_plano(consumo, /):
   # if consumo <= 10:
       # print("Plano Essencial Fibra - 50Mbps")
   # elif consumo <= 20 and consumo > 10:
       # print("Plano Prata Fibra - 100Mbps")
   # elif consumo >= 21: 
      #  print("Plano Premium Fibra - 300Mbps")


#def main():
   
     # consumo = float(input())
      #recomendar_plano(consumo)
       
    
#main()