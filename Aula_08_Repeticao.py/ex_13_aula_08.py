import os

os.system("cls")

print("Criar um algoritmo que leia a idade de 1000 pessoas. Exiba a quantidade de pessoas em cada classe eleitoral: ")
print("\n-Não eleitor - Abaixo de 16 anos")
print("-Obrigatório entre 18 e 65 anos")
print("-Eleitor Facultativo entre 16, 17 e maior de 65 anos\n")

naoEleitor = 0
eleitorObrigatorio = 0
eleitorFacultativo = 0

for pessoas in range(1, 1000 + 1):
    idade = int(input(f"Insira a {pessoas}ª idade entre 1 a 113 anos: "))

    while idade < 1 or idade > 113:
        idade = int(input("\nIncorreto!"
                          "\nInsira uma Idade válida: "))

    if idade < 16:
        naoEleitor = naoEleitor + 1
    else:
        if idade >= 18 and idade <= 65:
            eleitorObrigatorio = eleitorObrigatorio + 1
        else:
            eleitorFacultativo = eleitorFacultativo + 1
print(f"\nEntre 1.000 pessoas, de acordo com suas respectivas idades informadas, a classe eleitoral é:"
      f"\n"
      f"\nNão Eleitor: {naoEleitor}"
      f"\nEleitor Obrigatório: {eleitorObrigatorio}"
      f"\nEleitor Facultativo: {eleitorFacultativo}")
