import os

os.system("cls")

print("Programa que leia o código do item pedido, a quantidade e vá calculando o valor total a ser pago pelo pedido."
      "\nObs: Usar uma FLAG para continuar o programa.")

INICIO_DE_CARDAPIO = 100
FIM_DE_CARDAPIO = 105
CONTINUAR_PEDIDO = 1
ENCERRAR_PEDIDO = 2

CACHORRO_QUENTE = 2.50
BAURU_SIMPLES = 2.00
BAURU_COM_OVO = 3.50
HAMBURGER = 5.10
CHEESEBURGER = 3.30
REFRIGERANTE = 2.00

codigoDoItem = 0
quantidadeDoItem = 0
total = 0
flagDeContinuidadeDoPrograma = 0

while flagDeContinuidadeDoPrograma != ENCERRAR_PEDIDO:

    print("\nCardápio da Hamburgueria\n"
          "\nCódigo Lanche || Especificação ||   Preço\n"
          "[100]            Cachorro Quente    2,50\n"
          "[101]            Baurú Simples      2,00\n"
          "[102]            Baurú com Ovo      3,50\n"
          "[103]            Hamburger          5,10\n"
          "[104]            Cheeseburger       3,30\n"
          "[105]            Refrigerante       2,00")

    codigoDoItem = int(input("\nInforme qual item da lista você deseja adquirir: "))

    while codigoDoItem < INICIO_DE_CARDAPIO or codigoDoItem > FIM_DE_CARDAPIO:
        print("Comando inválido !")
        codigoDoItem = int(input("\nInforme qual item da lista você deseja adquirir: "))

    quantidadeDoItem = int(input("Digite a quantidade deste item: "))

    match codigoDoItem:
        case 100:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Cachorro Quente")
            total = total + CACHORRO_QUENTE * quantidadeDoItem
        case 101:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Baurú Simples")
            total = total + BAURU_SIMPLES * quantidadeDoItem

        case 102:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Baurú com Ovo")
            total = total + BAURU_COM_OVO * quantidadeDoItem

        case 103:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Hamburger")
            total = total + HAMBURGER * quantidadeDoItem

        case 104:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Cheeseburger")
            total = total + CHEESEBURGER * quantidadeDoItem

        case 105:
            print(f"\nVocê escolheu {quantidadeDoItem} unidade(s) do item: Refrigerante")
            total = total + REFRIGERANTE * quantidadeDoItem

    flagDeContinuidadeDoPrograma = int(input("\nDigite 1 = Sim // Digite 2 = Não"
                                             "\nDeseja continuar comprando? "))
    while flagDeContinuidadeDoPrograma != CONTINUAR_PEDIDO and flagDeContinuidadeDoPrograma != ENCERRAR_PEDIDO:
        print("Comando inválido")
        flagDeContinuidadeDoPrograma = int(input("\nDigite 1 = Sim // Digite 2 = Não"
                                                 "\nDeseja continuar comprando? "))
print(f"\nSeu pedido ficará com o valor de: {total:.2f}"
      "\nObrigado pela preferência!")