import os

os.system("cls")

print("\nPrograma que receba uma lista com 10 valores numéricos, gere uma nova lista onde cada"
      "elemento dessa lista é o quadrado dos elementos da primeira lista.\n")

LIMITE_DE_VALORES_NUMERICOS = 10

listaValoresNumericos = []
listaQuadradoDosValores = []

for index in range(LIMITE_DE_VALORES_NUMERICOS):
    listaValoresNumericos.append(int(input(f"Informe o {index + 1}º valor da lista: ")))

for indice in range(len(listaValoresNumericos)):
    elemento = listaValoresNumericos[indice]
    elemento = elemento ** 2
    listaQuadradoDosValores.append(elemento)

print(f"\nLista com o Quadrado de cada número informado: {listaQuadradoDosValores}")
