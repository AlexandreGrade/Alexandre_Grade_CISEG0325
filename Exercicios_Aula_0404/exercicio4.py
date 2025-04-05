saldo = float(input("Insira o saldo da conta: "))
cheque = float(input("Insira o valor do cheque: "))

if cheque <= saldo:
    saldo -= cheque
    print(f"Valor do cheque válido. Saldo atual: {saldo}")
else:
    print("Saldo insuficiente. Valor do cheque inválido.")