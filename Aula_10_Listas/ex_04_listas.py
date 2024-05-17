import os

os.system("cls")

print("\nPrograma que receba uma lista com 12 números e imprima quais são os números que estão armazenados nas "
      "posições de índice ímpar.\n")

LIMITE_DE_NUMEROS = 12
listaDeNumeros = []

for index in range(LIMITE_DE_NUMEROS):
    listaDeNumeros.append(int(input(f"Informe o {index + 1}º número da lista: ")))
print("")

for indice in range(len(listaDeNumeros)): #indice fará a iteração da listaDeNúmeros (0, 1, 2 ,3...)
                                          #e listaDeNúmeros já recebeu os elementos de cada posição.
    elemento = listaDeNumeros[indice]  #A variável elemento receberá a numeração da listaDeNúmeros.
    if indice % 2 != 0:  #Se a posiçao de indice for dividida por 2 e seu resto for diferente de 0, significa que a posição é ímpar.
        print(f"Número armazenado na posição impar: {elemento}")
