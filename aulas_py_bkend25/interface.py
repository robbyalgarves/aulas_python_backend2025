from calculo import dobro, triplo, quadrado, raiz_quadrada 


LISTA_OPCOES = ["1","2","3","8"]

def mostra_menu():
    print("""\n
    Digite a opção desejada:
    1- Calcular o dobro
    2- Calcular o triplo
    3- Calcular o quadrado
    8- Calcular a raiz cubica
    4- Finalizar""")

def analisa_opcao(opcao):
    if opcao == "1":
        numero = input("Iniciando cálculo do dobro... Digite o numero: ")
        dobronum = dobro(numero) # chamando a função dobro com o num do usuario
        print(f"O dobro de {numero} é {dobronum}")

    elif opcao == "2":
        numero = input("Iniciando cálculo do triplo... Digite o numero: ")
        triplonum = triplo(numero) # chamando a função triplo com o num do usuario
        print(f"O triplo de {numero} é {triplonum}")

    elif opcao == "3":
        numero = input("Iniciando cálculo do quadrado... Digite o numero: ")
        quadradonum = quadrado(numero) # chamando a função quadrado com o num do usuario
        print(f"O quadrado de {numero} é {quadradonum}")

    elif opcao == "8":
        numero = input("Iniciando cálculo do raiz_quadrada... Digite o numero: ")
        raiz_quadradanum = raiz_quadrada(numero) # chamando a função raiz_quadrada com o num do usuario
        print(f"O raiz_quadrada de {numero} é {raiz_quadradanum}")

   