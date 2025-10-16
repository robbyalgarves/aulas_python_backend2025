import interface
from interface import dobro, triplo, quadrado

start = input("Digite sim para iniciar ou não para parar: ")

def menu():

    while True:
        escolha = int(input('''Digite a opção desejada: "
        1- Calcular o dobro
        2- Calcular o triplo 
        3- Calcular o quadrado 
        4- para SAIR: '''
        ))

        if  escolha == 1:
            numero = int(input("Digite um número: "))
            dobro = interface.dobro(numero)
            print(f"O dobro de {numero} é {dobro}")

        if escolha == 2:
            numero1 = int(input("Digite um número: "))
            triplo = interface.triplo(numero1)
            print(f"O triplo de {numero1} é {triplo}")
            
        elif escolha == 3:
            numero2 = int(input("Digite um número: "))
            quadrado = interface.quadrado(numero2)
            print(f"O quadrado de {numero2} é {quadrado}")

        elif escolha == 4:
            print("SAIR")
            break

        else:
            print("Digite o número correto!")
            continue

if start == "sim":
    menu()