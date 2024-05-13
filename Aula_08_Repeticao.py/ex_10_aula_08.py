import os
os.system ("cls")

print("Programa que recebe N números e conta quantos destes números são pares\n")

numeros = int(input("Informe a quantidade de números: "))
pares = 0

for cont in range (1, numeros+1):
    num = int(input(f"Digite o {cont}° número: "))
    if num % 2 == 0:
        pares = pares +1
        
print(f"\nQuantidade de Números Pares: {pares}")
