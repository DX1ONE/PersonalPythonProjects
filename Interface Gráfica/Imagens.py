from tkinter import *

janela = Tk()

imagem1 = PhotoImage(file='IF Python teste imagens 1.png.png')
fundo = Label(janela, image=imagem1)
fundo.place(x=0, y=0)

imagem2 = PhotoImage(file='IF_Python_teste_imagens_2-removebg-preview.png')
pessoa = Label(janela, image=imagem2)
pessoa.place(x=30, y=50)

imagem3 = PhotoImage(file='IF_Python_teste_imagens_3-removebg-preview.png')
globo = Label(janela, image=imagem3)
globo.place(x=330, y=50)


janela.geometry('626x417+0+0')
janela.mainloop()