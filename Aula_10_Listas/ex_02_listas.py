import os

os.system("cls")

print("Programa que receba uma lista com 8 números inteiros e imprima os elementos pares.\n")

LIMITE_NUMEROS_INTEIROS = 8
lista_numeros = []

for index in range(LIMITE_NUMEROS_INTEIROS):
    lista_numeros.append(int(input(f"Digite o {index + 1}º número: ")))

print("\nNúmeros Pares:")
for elemento in lista_numeros:
    if elemento % 2 == 0:
        print(elemento)
