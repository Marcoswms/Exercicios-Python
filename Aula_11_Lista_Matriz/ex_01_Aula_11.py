import os

os.system("cls")

print("A Companhia de Taxi LocalCerto armazena os dados de seus motoristas(codigo,nome, número do taxi e Kper)."
      "\nFaça um programa que seja capaz de ler os dados de n (máximo de 20) motoristas (utilizar uma lista de lista)."
      "\nEm seguida, o programa deve imprimir um relatório conforme o modelo abaixo."
      "\nCódigo    Motorista     Nº Taxi   Valor a Receber"
      "\n XXXX      XXXXX        XXXXX       XXXXXX"
      "\nO valor a receber é calculado multiplicando-se a quantidade Kper (Kilometro percorrido) por R$ 1,20."
      "\nAo final o programa deve também exibir todos os dados do motorista com maior valor a receber.")

POSICAO_NOME_MOTORISTA = 0
POSICAO_NUMERO_TAXi = 1
POSICAO_KPER = 2
POSICAO_VALOR_A_RECEBER = 3
LIMITE_DE_CADASTRO = 3  # Deixei 3 para testes, mas são 20 cadastros

listaDadosMotorista = []
contadorMotorista = 0
codigoPosicaoMotorista = 0

posicaoMaiorValor = 0
while contadorMotorista < LIMITE_DE_CADASTRO:
    nomeMotorista = input(f"\nInforme o nome do {contadorMotorista + 1}º Motorista para cadastro: ").title()
    numeroTaxi = int(input("Informe o número do Taxi (Ex: 001):"))
    kper = float(input("Informe a Quantidade de Kilômetro Percorrido: (Ex: 20.000 )"))
    valorAreceber = 0
    contadorMotorista += 1

    dadosMotorista = [nomeMotorista, numeroTaxi, kper, valorAreceber]
    listaDadosMotorista.append(dadosMotorista)

for index in range(len(listaDadosMotorista)):
    recebeLista = listaDadosMotorista[index]
    recebeKper = recebeLista[POSICAO_KPER]
    recebeLista[POSICAO_VALOR_A_RECEBER] = recebeKper * 1.20
    maiorValor = listaDadosMotorista[posicaoMaiorValor]
    if maiorValor[POSICAO_VALOR_A_RECEBER] < recebeLista[POSICAO_VALOR_A_RECEBER]:
        posicaoMaiorValor = index
    codigoPosicaoMotorista += 1
    print(f"Código     Motorista      NºTaxi      Valor a Receber"
          f"\n  {codigoPosicaoMotorista}        {recebeLista[POSICAO_NOME_MOTORISTA]}        {recebeLista[POSICAO_NUMERO_TAXi]:.2f}        "
          f" {recebeLista[POSICAO_VALOR_A_RECEBER]:.2f}")
maiorValor = listaDadosMotorista[posicaoMaiorValor]
print(f"\nO cadastro com maior valor a receber é:"
      f"\nMotorista: {listaDadosMotorista[posicaoMaiorValor][POSICAO_NOME_MOTORISTA]} - NºTaxi: {listaDadosMotorista[posicaoMaiorValor][POSICAO_NUMERO_TAXi]} - Valor a Receber: {listaDadosMotorista[posicaoMaiorValor][POSICAO_VALOR_A_RECEBER]}")
