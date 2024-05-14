import os

os.system("cls")

print("\nPrograma que simule um jogo de adivinhação:\n"
      "\n* O jogador 1 escolhe um número entre 1 e 10:"
      "\n* O jogador 2 insere números na tentativa de acertar o número escolhido pelo jogador 1"
      "\n* Quando ele acertar, o algoritmo deve informar que ele acertou o número escolhido pelo jogador 1 em x tentativas\n")

LIMITE_INICIAL_DE_NUMERO = 1
LIMITE_FINAL_DE_NUMERO = 10
tentativa = 1

jogador01 = int(input("Jogador 01 - Escolha um número entre 1 e 10: "))

while jogador01 < LIMITE_INICIAL_DE_NUMERO or jogador01 > LIMITE_FINAL_DE_NUMERO:
    jogador01 = int(input("Somente números entre 1 e 10: "))
os.system("cls")

jogador02 = int(input("\nJogador 02 - Adivinhe qual número entre 1 e 10 o jogador 01 escolheu: "))

while jogador02 < LIMITE_INICIAL_DE_NUMERO or jogador02 > LIMITE_FINAL_DE_NUMERO:
    jogador01 = int(input("Somente números entre 1 e 10: "))

while jogador01 != jogador02:
    jogador02 = int(input("Você errou !\nTente novamente: "))
    tentativa = tentativa + 1

    while jogador02 < LIMITE_INICIAL_DE_NUMERO or jogador02 > LIMITE_FINAL_DE_NUMERO:
        jogador02 = int(input("Somente números entre 1 e 10: "))

print(f"\nParabéns, você acertou !!\n"
      f"\n* Número escolhido pelo Jogador 01: {jogador01}"
      f"\n* Número de tentativas utilizadas pelo Jogador 02: {tentativa}")