import os

os.system("cls")

print("\nPrograma que que receba uma lista com 9 valores numéricos, calcule e mostre a somatória dos números pares.\n")

LIMITE_VALORES_NUMERICOS = 9

listaEntradaDeValores = []
listaDePares = []

for index in range(LIMITE_VALORES_NUMERICOS):
    listaEntradaDeValores.append(int(input(f"Informe o {index + 1}º valor da lista: ")))

for elemento in listaEntradaDeValores:
    if elemento % 2 == 0:
        listaDePares.append(elemento)

somaListaPares = sum(listaDePares)
print(f"\nA somatória dos números pares é igual á: {somaListaPares}")
