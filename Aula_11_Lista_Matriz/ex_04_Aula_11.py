import os

os.system("cls")

print("Dado a lista que recebe o Nome, Sexo, Idade e Altura.\n"
      "Faça um programa que leia esses dados até que o usuário queira parar e determine:"
      "\na) altura da pessoa mais alta;"
      "\nb) nome, sexo e idade da pessoa mais nova;"
      "\nc) média de idade dos 'baixinhos', altura <= 1,58 cm;"
      "\nd) quantidades de mulheres com idade superior ou igual a 20.")

POSICAO_NOME = 0
POSICAO_GENERO = 1
POSICAO_IDADE = 2
POSICAO_ALTURA = 3
ENCERRA_PROGRAMA = "Fim"
GENERO_MASCULINO = "Masculino"
GENERO_FEMININO = "Feminino"
MEDIA_ALTURA = 1.58

listaMaeDeDadosCadastrados = []

decideAcaoDoPrograma = ""
contadorQuantidadeCadastrados = 0
contadorMediaIdade = 0
maiorAltura = 0

nomeDoMaisNovo = []
generoDoMaisNovo = []
nomeComMesmaIdade = []
listaNomes = []

while True:
    recebeNome = input(f"\nInforme o {contadorQuantidadeCadastrados + 1}º nome a ser cadastrado: ").title()
    recebeGenero = input(f"Informe o genero do(a) {recebeNome} de acordo com a alternativa abaixo:"
                         "\n1 - Masculino"
                         "\n2 - Feminino"
                         "\nEscolha: ")

    while recebeGenero != "1" and recebeGenero != "2":
        recebeGenero = input("\nComando Inválido!"
                             f"\nInforme o genero do(a) {recebeNome} de acordo com a alternativa abaixo:"
                             "\n1 - Masculino"
                             "\n2 - Feminino"
                             "\nEscolha: ")
    match recebeGenero:
        case "1":
            recebeGenero = GENERO_MASCULINO
        case "2":
            recebeGenero = GENERO_FEMININO

    recebeIdade = int(input(f"Informe a Idade do(a) {recebeNome}: "))
    recebeAltura = float(input(f"Informe a Altura do(a) {recebeNome}: "))

    posicaoDeDados = [recebeNome, recebeGenero, recebeIdade, recebeAltura]
    listaMaeDeDadosCadastrados.append(posicaoDeDados)

    contadorQuantidadeCadastrados += 1
    decideAcaoDoPrograma = input("\nDigite [1] para Novo Cadastro"
                                 "\nDigite [2] para Finalizar o cadastro"
                                 "\nEscolha: ")
    while decideAcaoDoPrograma != "1" and decideAcaoDoPrograma != "2":
        decideAcaoDoPrograma = input("\nComando Inválido!"
                                     "\nDigite [1] para Novo Cadastro"
                                     "\nDigite [2] para Finalizar o cadastro "
                                     "\nEscolha: ")
    match decideAcaoDoPrograma:
        case "2": decideAcaoDoPrograma = ENCERRA_PROGRAMA
    if decideAcaoDoPrograma == ENCERRA_PROGRAMA:
        break

posicaoUsuarioMaisAlto = 0  # Salvar a posição do elemento que representa o usuário mais alto
posicaoUsuarioMaisNovo = 0
somaIdadeUsuariosBaixinhos = 0
contadorUsuariosBaixinhos = 0
contadorMulheresMaiorQue20 = 0

for index in range(len(listaMaeDeDadosCadastrados)):
    usuario = listaMaeDeDadosCadastrados[index]
    usuarioMaisAlto = listaMaeDeDadosCadastrados[posicaoUsuarioMaisAlto]
    if usuarioMaisAlto[POSICAO_ALTURA] < usuario[POSICAO_ALTURA]:
        posicaoUsuarioMaisAlto = index
    usuarioMaisNovo = listaMaeDeDadosCadastrados[posicaoUsuarioMaisNovo]
    if usuarioMaisNovo[POSICAO_IDADE] > usuario[POSICAO_IDADE]:
        posicaoUsuarioMaisNovo = index
    if usuario[POSICAO_ALTURA] <= MEDIA_ALTURA:
        somaIdadeUsuariosBaixinhos += usuario[POSICAO_IDADE]
        contadorUsuariosBaixinhos += 1
    if usuario[POSICAO_GENERO] == GENERO_FEMININO and usuario[POSICAO_IDADE] >= 20:
        contadorMulheresMaiorQue20 += 1

print(f"\nA altura do usuário mais alto é: {listaMaeDeDadosCadastrados[posicaoUsuarioMaisAlto][POSICAO_ALTURA]}")
usuarioMaisNovo = listaMaeDeDadosCadastrados[posicaoUsuarioMaisNovo]
print(
    f"\nPessoa(s) mais nova(s) cadastrada(s): {usuarioMaisNovo[POSICAO_NOME]} - Gênero: {usuarioMaisNovo[POSICAO_GENERO]} - Idade: {usuarioMaisNovo[POSICAO_IDADE]}")
mediaDeIdadeUsuariosBaixinhos = 0
if somaIdadeUsuariosBaixinhos > 0:
    mediaDeIdadeUsuariosBaixinhos = somaIdadeUsuariosBaixinhos / contadorUsuariosBaixinhos
print(f"\nMedia de idade de usuários menores que {MEDIA_ALTURA} é de: {mediaDeIdadeUsuariosBaixinhos:.0f}")
print(f"\nQuantidade de Mulheres com 20 anos ou mais: {contadorMulheresMaiorQue20}")