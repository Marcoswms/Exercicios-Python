import os

os.system("cls")

print("Programa que receba uma lista com 10 números e imprima os números maiores do que 15.\n")

LIMITE_DE_VALORES_NUMERICOS = 10
lista_numeros = []

for index in range(LIMITE_DE_VALORES_NUMERICOS):
    lista_numeros.append(int(input(f"Digite o {index + 1}º número: ")))

print(f"\nNúmeros maiores de 15 listados abaixo: ")

for index in range(10):
    if lista_numeros[index] > 15:
        print(lista_numeros[index])
