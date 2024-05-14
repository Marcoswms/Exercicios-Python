import os
os.system ("cls")

print("Programa que calcule, quantos anos serão necessários para que a população do país A, ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.")

populacaoA = 98.000000
populacaoB = 200.0000000
contador = 0

while populacaoA < populacaoB:
    populacaoA = populacaoA + populacaoA * 3.5 / 100
    populacaoB = populacaoB + populacaoB * 1.5 /100

    contador += 1

print(f"\nSerá necessário {contador} anos para a população A ultrapassar ou se igualar a população B")





