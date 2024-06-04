import os
import time

os.system("cls")

print("Elabore um programa que entre com os dados de n pessoas (nome, rg, sexo,idade)"
      "Utilizar uma lista para armazenar esses dados. Em seguida, o programa deve exibir um relatório contendo todos os"
      " dados das pessoas do sexo feminino com mais de 30 anos.")
POSICAO_NOME = 0
POSICAO_RG = 1
POSICAO_GENERO = 2
POSICAO_IDADE = 3
FEMININO_COM_MAIS_DE_30 = 30
GENERO_MASCULINO = "Masculino"
GENERO_FEMININO = "Feminino"
FIM_DO_PROGRAMA = "Fim"

listaMaeDadosCadastrados = []
contadorDeCadastrados = 0
while True:
    nome = input(f"\nInforme o {contadorDeCadastrados + 1}º nome para ser cadastrado: ").title()
    rg = int(input(f"\nInforme o RG do(a) {nome}: "))
    genero = input("\n1 - Masculino"
                   "\n2 - Feminino"
                   "\nInforme o Gênero de acordo com a numeração acima: ")
    match genero:
        case "1":
            genero = "Masculino"
        case "2":
            genero = "Feminino"
    idade = int(input(f"\nInforme a idade: "))
    contadorDeCadastrados += 1

    decideAcao = input("\nDeseja continuar cadastrando?"
                       "\n1 - Sim"
                       "\n2 - Não"
                       "\nEscolha: ")
    armazenaDados = (nome, rg, genero, idade)
    listaMaeDadosCadastrados.append(armazenaDados)
    match decideAcao:
        case "1":
            print("\nVamos continuar com o cadastro")
            time.sleep(1.5)
        case "2":
            print("\nObrigado pela preferência!\n"
                  "\nSerá exibido um relatório contendo os dados de pessoas do gênero "
                  "Feminino com mais de 30 anos.")
            time.sleep(1.5)
            decideAcao = FIM_DO_PROGRAMA
            if decideAcao == FIM_DO_PROGRAMA:
                break
for index in range(len(listaMaeDadosCadastrados)):
    recebeLista = listaMaeDadosCadastrados[index]
    comparaIdade = recebeLista[POSICAO_IDADE]
    comparaGenero = recebeLista[POSICAO_GENERO]
    if comparaGenero == GENERO_FEMININO and comparaIdade > FEMININO_COM_MAIS_DE_30:
        recebeNome = recebeLista[POSICAO_NOME]
        recebeRg = recebeLista[POSICAO_RG]
        recebeIdade = recebeLista[POSICAO_IDADE]
        print(f"Nome: {recebeNome} - Rg: {recebeRg} - Idade {recebeIdade}")
