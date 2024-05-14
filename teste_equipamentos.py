#def main():: Define a função principal do programa, chamada main. Esta função conterá a lógica principal do programa.
#equipamentos = []: Inicializa uma lista vazia chamada equipamentos. Esta lista será usada para armazenar os nomes dos equipamentos inseridos pelo usuário.
    
def main():

    equipamentos = []

#max_equipamentos = 3: Define uma variável chamada max_equipamentos e atribui a ela o valor 3. Isso representa o número máximo de equipamentos que o usuário pode inserir.
    max_equipamentos = 3

#for i in range(max_equipamentos):: Inicia um loop for que irá iterar max_equipamentos vezes (neste caso, 3 vezes). A variável i será usada como índice do loop, variando de 0 a 2.
#equipamento = input(f"Insira o nome do equipamento {i+1}: "): Solicita ao usuário que insira o nome de um equipamento. O input() exibe uma mensagem pedindo a entrada do equipamento número i+1 (o f"Insira o nome do equipamento {i+1}: " é uma f-string que formata a string para incluir o valor de i+1). A entrada do usuário é armazenada na variável equipamento.
#equipamentos.append(equipamento): Adiciona o equipamento inserido pelo usuário à lista equipamentos usando o método append.
   
   
    for i in range(max_equipamentos):

        equipamento = input(f"")
        equipamentos.append(equipamento)

#print("\nLista de equipamentos cadastrados:"): Exibe uma mensagem no console indicando que a lista de equipamentos será mostrada. O \n adiciona uma nova linha antes da mensagem para separação visual.
#for equipamento in equipamentos:: Inicia um loop for que itera sobre cada item na lista equipamentos.
#print(f"- {equipamento}"): Para cada equipamento na lista, exibe o nome do equipamento precedido por um hífen (-). Novamente, a f-string é usada para formatar a string.

    print("\n Lista de Equipamentos:")
    for equipamento in equipamentos:
        print(f"- {equipamento}")
   
      
       
    
main()
