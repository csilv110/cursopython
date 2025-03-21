while True:
    nota1bim = float(input("Digite a nota 1 Bim: "))
    if (nota1bim <= 10) and (nota1bim >= 0):
     break

nota2bim = float(input("Digite a nota 2 Bim? "))
while True:
    nota2bim = float(input("Digite a nota 2 Bim: "))
    if (nota2bim <= 10) and (nota2bim >= 0):
     break
nota3bim = float(input("Digite a nota 3 Bim? "))
while True:
    nota3bim = float(input("Digite a nota 3 Bim: "))
    if (nota3bim <= 10) and (nota3bim >= 0):
     break
nota4bim = float(input("Digite a nota 4 Bim? "))
while True:
    nota4bim = float(input("Digite a nota 4 Bim: "))
    if (nota4bim <= 10) and (nota4bim >= 0):
     break

Media = (nota1bim + nota2bim + nota3bim + nota4bim) /4

print(f"Sua média é {Media:,.2f}")

if (Media >= 5):
    print("ALUNO APROVADO!!!")    
elif (Media >=3):
    print("Aluno em recuperação")
else:
    print("ALUNO REPROVADO!!!")

print("fim do ano letivo")