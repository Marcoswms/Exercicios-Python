

print("Programa que recebe duas notas de 60 alunos, calcula a Média Individual e mostre quantos foram Aprovados, Reprovados e ficaram para Exame\n")

aprovados = 0
exame = 0
reprovados = 0

for alunos in range (1, 60+1):
    nota1 = float(input(f"Informe a Primeira nota do {alunos}° aluno: "))
    nota2 = float(input(f"Informe a Segunda nota do {alunos}° aluno: "))
    
    media = (nota1 + nota2) / 2
    if media < 3:
        reprovados = reprovados + 1
    else:
        if media < 5:
            exame = exame + 1
        else:
            aprovados = aprovados + 1
print(f"\nEntre 60 alunos: \nAprovados: {aprovados}\nFicaram para Exame: {exame}\nReprovados: {reprovados}")



