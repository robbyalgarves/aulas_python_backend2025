# Lista para armazenar os empréstimos
emprestimos = []

# Loop de cadastro
while True:
    usuario = input("Digite o nome do usuário (ou 'SAIR' para encerrar): ")
    if usuario.upper() == "SAIR":
        break
    livro = input("Digite o nome do livro emprestado: ")
    
    # Cria um dicionário com os dados e adiciona à lista
    registro = {"usuario": usuario, "livro": livro}
    emprestimos.append(registro)

# Loop para exibir o relatório de empréstimos
print("\nRelatório de Empréstimos:")
for emprestimo in emprestimos:
    print(f"Usuário: {emprestimo['usuario']} - Livro: {emprestimo['livro']}")