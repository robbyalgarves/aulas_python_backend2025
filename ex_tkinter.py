from tkinter import Tk, Button, Label   #TK Cria a janela e Button cria o botão e Label cria o rótulo
def dizer_ola():
    rotulo_ola_mundo.config(text = "Olá, Mundo!")
                            
janela = Tk()
janela.title("Dizer Olá")
janela.maxsize(width=200, height=200)

botao_dizer_ola = Button(janela, text = "Dizer Olá", command = dizer_ola)
botao_dizer_ola.pack(pady = 20)

rotulo_ola_mundo = Label(janela,text = "")
rotulo_ola_mundo.pack()

janela.mainloop() 
