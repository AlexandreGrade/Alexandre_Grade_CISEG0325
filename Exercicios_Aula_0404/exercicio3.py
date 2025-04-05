num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    print(f"Ordem decrescente: {num1}, {num2}")
else:
    print(f"Ordem decrescente: {num2}, {num1}")

if num1 < num2:
    print(f"Ordem crescente: {num1}, {num2}")
else:
    print(f"Ordem crescente: {num2}, {num1}")