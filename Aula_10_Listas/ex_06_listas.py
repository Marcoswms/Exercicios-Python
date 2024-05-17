import os

os.system("cls")

print("\nPrograma que leia 15 números inteiros. Determina e mostra quantas vezes o número 0 é repetido na lista\n")

LIMITE_DE_VALORES_NUMERICOS = 15

listaValoresNumericos = []
contadorZero = 0

for index in range(LIMITE_DE_VALORES_NUMERICOS):
    listaValoresNumericos.append(int(input(f"Informe o {index + 1}º número: ")))

for indice in range(len(listaValoresNumericos)):
    elemento = listaValoresNumericos[indice]

    if elemento == 0:
        contadorZero += 1

print(f"\nO número 0 aparece {contadorZero} vez(es) nesta lista")