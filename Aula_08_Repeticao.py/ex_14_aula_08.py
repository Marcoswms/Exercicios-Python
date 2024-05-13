

print("Programa para o Usuário escolher a Tabuada que deseja imprimir!!\n")

tabuada = int(input("Insira o número para obter sua Tabuada: "))
print ("")
for multiplicar in range (1, 10+1):
    total = tabuada * multiplicar
    print(f"{tabuada} x {multiplicar} = {total}")
print("\nFim")

