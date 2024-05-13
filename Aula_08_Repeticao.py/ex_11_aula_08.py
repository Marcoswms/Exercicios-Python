import os
os.system ("cls")

print("Programa que imprime na tela os números de 1 a 1000 exceto os números múltiplos de 3")

for cont in range (1, 1000+1):
    total = cont % 3
    if total != 0:
        print(cont)
