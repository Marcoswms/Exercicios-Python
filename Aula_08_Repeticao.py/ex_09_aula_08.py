import os
os.system ("cls")

print("Programa  que receba duas notas de 10 alunos e calcule a média para cada um deles e exiba a média individual dos alunos e a média total")

sm = 0
for cont in range (1, 10+1):
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    media =  (n1 + n2)/2
    print(f"A média individual é de {media}")
    sm = sm + media 
mg = sm/10
print(f"A média geral é de {mg}")