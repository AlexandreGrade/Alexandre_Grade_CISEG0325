def validar_nome(nome):
    """Valida se o nome tem a primeira letra maiúscula e o resto minúsculo, incluindo acentuação."""
    return nome[0].isupper() and nome[1:] == nome[1:].lower()


def adicionar_pessoa(lista):
    primeiro_nome = input("Digite o primeiro nome: ").strip()
    if not validar_nome(primeiro_nome):
        print("Primeiro nome inválido! Exemplo válido: João")
        return
    ultimo_nome = input("Digite o último nome: ").strip()
    if not validar_nome(ultimo_nome):
        print("Último nome inválido! Exemplo válido: Silva")
        return
    try:
        idade = int(input("Digite a idade: "))
    except ValueError:
        print("Idade inválida!")
        return
    lista.append({"primeiro": primeiro_nome, "ultimo": ultimo_nome, "idade": idade})
    print("Pessoa adicionada com sucesso!")


def remover_por_nome(lista, tipo):
    nome = input(f"Digite o {tipo} nome a remover: ").strip()
    encontrados = [p for p in lista if p[tipo] == nome]
    if not encontrados:
        print(f"Nenhum {tipo} nome encontrado com '{nome}'!")
        return
    for p in encontrados:
        lista.remove(p)
        print(f"{p['primeiro']} {p['ultimo']} removido com sucesso!")


def listar_ordenado(lista, tipo):
    def ascii_sort_key(pessoa):
        return [ord(c) for c in pessoa[tipo]]

    lista_ordenada = sorted(lista, key=ascii_sort_key)
    print(f"\nLista ordenada por {tipo} nome:")
    for p in lista_ordenada:
        print(f"{p['primeiro']} {p['ultimo']} - {p['idade']} anos")


def menu():
    lista = []
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar pessoa")
        print("2. Listar por primeiro nome")
        print("3. Listar por último nome")
        print("4. Remover por primeiro nome")
        print("5. Remover por último nome")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoa(lista)
        elif opcao == "2":
            listar_ordenado(lista, "primeiro")
        elif opcao == "3":
            listar_ordenado(lista, "ultimo")
        elif opcao == "4":
            remover_por_nome(lista, "primeiro")
        elif opcao == "5":
            remover_por_nome(lista, "ultimo")
        elif opcao == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")


menu()