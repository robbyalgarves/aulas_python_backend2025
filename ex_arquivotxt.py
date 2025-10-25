# Programa de cadastro simples

def cadastrar_contato():
    print("=== CADASTRO DE CONTATO ===")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")

    # Abre o arquivo para adicionar (modo append)
    with open("dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Telefone: {telefone}\n")
        arquivo.write(f"E-mail: {email}\n")
        arquivo.write(f"Endereço: {endereco}\n")
        arquivo.write("-" * 40 + "\n")

    print("\nContato cadastrado com sucesso!\n")

# Programa principal
    cadastrar_contato()