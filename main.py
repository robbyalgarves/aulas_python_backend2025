import calculo


print("Olá, mundo agora no VScode!!!\n")
print("programa do dobro")
print("_" * 50)

x = input("Digite o numero e vou dizer o dobro: ")

dobro = calculo.dobro(x)

print(f"o dobro de {x} é {dobro}")

y= input("Agora , digite outro numero e direi o seu triplo") 

triplo = calculo.triplo(y)

print(f"O triplo de {y} é {triplo}")
