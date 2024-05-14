import os

os.system("cls")

print("\nPrograma para um funcionário cadastrar o controle de qualidade de uma Fábrica.\n"
      "\n- A fábrica produz 400 peças por dia;"
      "\n- Cadastrar o número da peça e seu estado (Aprovado ou Reprovado);"
      "\n- Imprimir os números das peças reprovadas;"
      "\n- Imprimir o total de peças aprovadas e reprovadas no final do dia.")

LIMITE_FINAL_PECAS_PRODUZIDAS = 4
LIMITE_INICIAL_PECAS_PRODUZIDAS = 1
STATUS_PECA_APROVADA = 1
STATUS_PECA_REPROVADA = 2

listaPecaReprovada = []
numeroDaPeca = 0
contadorReprovado = 0
contadorAprovado = 0

for index in range(LIMITE_FINAL_PECAS_PRODUZIDAS):
    numeroDaPeca = int(input(f"\nDigite a numeração da {index + 1}ª Peça a ser cadastrada: "))

    while numeroDaPeca < LIMITE_INICIAL_PECAS_PRODUZIDAS or numeroDaPeca > LIMITE_FINAL_PECAS_PRODUZIDAS:
        numeroDaPeca = int(input("\nIncorreto!!"
                                 f"\nDigite novamente a numeração da {index +1}ª Peça a ser cadastrada: "))
    validacaoPeca = int(input("\nEstado da Peça:\n"
                              "\n* Peças Aprovadas - Digite 1"
                              "\n* Peças Reprovadas - Digite 2:\n"
                              "\n* Escolha uma das alternativas acima: "))
    while validacaoPeca != STATUS_PECA_APROVADA and validacaoPeca != STATUS_PECA_REPROVADA:
        validacaoPeca = int(input("\nAlternativa Inválida!" 
                                  "\n* Peças Aprovadas - Digite 1"
                                  "\n* Peças Reprovadas - Digite 2\n"
                                  "\nEscolha uma das alternativas acima: "))
    if validacaoPeca.__eq__(STATUS_PECA_APROVADA):
        contadorAprovado += 1
    else:
        listaPecaReprovada.append(numeroDaPeca)
        contadorReprovado += 1

total = contadorAprovado + contadorReprovado
print(f"\nTotal de peças aprovadas: {contadorAprovado}"
      f"\nTotal de peças reprovadas: {contadorReprovado}"
      f"\nTotal de peças cadastradas: {total}"
      f"\nNúmero de peças reprovadas: {listaPecaReprovada}")
