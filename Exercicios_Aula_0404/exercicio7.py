nota1 = int(input("Insira a primeira nota(0 a 10): "))
nota2 = int(input("Insira a segunda nota(0 a 10): "))
nota3 = int(input("Insira a terceira nota(0 a 10): "))

peso1 = 2
peso2 = 3
peso3 = 5

soma_pesos = peso1 + peso2 + peso3
soma = (nota1*peso1) + (nota2*peso2) + (nota3*peso3)
media = soma / soma_pesos

print(f"Média: {media:.2f}")
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")