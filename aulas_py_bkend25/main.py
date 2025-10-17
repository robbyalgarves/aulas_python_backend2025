from interface import mostra_menu, analisa_opcao, LISTA_OPCOES


while True:
    print("BEM-VINDO A CALCULADORA SENAI")

    mostra_menu()

    opcao = input("Digite a opção desejada: ")

    if opcao == "4":
        print("-- ENCERRANDO PROGRAMA... ") 
        break       


    elif opcao not in LISTA_OPCOES:       # ALTERNATIVA: opcao != "1" and opcao != "2" and opcao != "3"
        print("Opção invalida! \n")
        continue    

    else:
        analisa_opcao(opcao)