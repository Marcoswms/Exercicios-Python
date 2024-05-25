import os

os.system("cls")

print("Faça um programa que leia uma lista que receba o nome, idade e sexo de pessoas"
      "até que o usuário digite fim no nome. Após a leitura faça:"
      "\na) Imprima o Nome, idade e sexo das pessoas cuja idade seja maior que a idade da primeira pessoa."
      "\nb) Imprima o Nome e idade de todas as mulheres."
      "\nc) Imprima o Nome dos homens menores de 21 anos.")

POSICAO_NOME = 0  # Posição do 1º dado
POSICAO_IDADE = 1  # Posição do 2º dado
POSICAO_GENERO = 2  # Posição do 3º dado
HOMENS_MENORES_21 = 21
GENERO_MASCULINO = "Masculino"
GENERO_FEMININO = "Feminino"
TERMINA_CADASTRO = "Fim"

usuariosCadastrados = []  # Lista "Mãe" - Onde todos os dados ficarão armazenados como um "Banco de dados"

while True:
    nome = input("\nDigite o nome do novo usuário(a): ").title()  # .title Transforma as primeiras letras em Maiúsculas
    if nome == TERMINA_CADASTRO:
        break
    idade = int(input(f"Digite a idade do usuário(a) {nome}: "))
    opcaoGenero = input(f"\nQual é o genero do usuário(a) {nome}?"
                        "\n1 - Masculino"
                        "\n2 - Feminino"
                        "\nDigite a opção: ")
    while opcaoGenero != "1" and opcaoGenero != "2":
        print("Opção incorreta!")
        opcaoGenero = input(f"\nQual é o genero do usuário(a) {nome}?"
                            "\n1 - Masculino"
                            "\n2 - Feminino"
                            "\nDigite a opção: ")
    genero = ""
    match opcaoGenero:
        case "1":
            genero = GENERO_MASCULINO
        case "2":
            genero = GENERO_FEMININO
    # Criacao de uma nova lista
    novoUsuario = [nome, idade, genero]  # Lista base - Para unir os 3 dados contidos nas 3 variáveis
    usuariosCadastrados.append(novoUsuario)  # Adiciona a Lista base com 3 posiçoes (Dentro da estrutura de repetição)

idadePrimeiroUsuario = usuariosCadastrados[0][POSICAO_IDADE]  # Recebe a lista 0 (O primeiro conjunto de dados a ser
# cadastrados) e a posição 1 desta lista, que é o dado na"Posição Idade".

print(f"\nUsuários com idade maior que {idadePrimeiroUsuario}: ")

for index in range(1, len(usuariosCadastrados)):
    proximoUsuario = usuariosCadastrados[index]  # Recebe a lista de cadastrados a partir do 2º cadastrado em diante.
    idadeProximoUsuario = proximoUsuario[POSICAO_IDADE]  # Recebe o elemento da posição Idade(1)
    if idadeProximoUsuario > idadePrimeiroUsuario:
        nomeProximoUsuario = proximoUsuario[POSICAO_NOME]  # Recebe a posição Nome(0)
        generoProximoUsuario = proximoUsuario[POSICAO_GENERO]  # Recebe a posição Genero(2)

        print(f"Nome: {nomeProximoUsuario}, Idade: {idadeProximoUsuario}, Genero: {generoProximoUsuario}")

print("\nUsuários do Gênero Feminino: ")
for index in range(len(usuariosCadastrados)):
    listaCadastrados = usuariosCadastrados[index]
    generoFeminino = listaCadastrados[POSICAO_GENERO]
    if generoFeminino == GENERO_FEMININO:
        nomeUsuario = listaCadastrados[POSICAO_NOME]
        idadeUsuario = listaCadastrados[POSICAO_IDADE]
        print(f"Nome: {nomeUsuario}, Idade: {idadeUsuario}, Gênero: {generoFeminino}")

print("\nUsuários do Gênero Masculino que possuem menos de 21 anos:")
for index in range(len(usuariosCadastrados)):
    listaCadastrados = usuariosCadastrados[index]
    idadeHomensMenoresDe21 = listaCadastrados[POSICAO_IDADE]
    generoHomensMenoresDe21 = listaCadastrados[POSICAO_GENERO]
    if idadeHomensMenoresDe21 < HOMENS_MENORES_21 and generoHomensMenoresDe21 == GENERO_MASCULINO:
        nomeUsuario = listaCadastrados[POSICAO_NOME]
        print(f"Nome: {nomeUsuario}")