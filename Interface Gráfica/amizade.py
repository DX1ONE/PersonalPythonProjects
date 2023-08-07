import requests
from tkinter import *
from random import choice


def amigos():
    lista = ['P iadista \n    I ntelijente \n             M etebalatiamu \n      E ngraçador\nN arcos \n             T entadordas08 \n                    A leijadinhodeamor','     S entafofo \n     M etefraco\n    I ludefeias\n      T rabaiador \n       H eroidas07', 'D iliça \n         I gnoramte \n         O marlindo \n     G ostoso \n      O reidelas']
    amg = choice(lista)
    texto_amigos['text'] = amg


janela = Tk()
janela.title('A Amizade é tudo')
janela.geometry('400x400')

# Texto_Orientação
texto_orientacao = Label(janela, text='Clique No Botão Para Sortear Um Brother')
texto_orientacao.grid(column=0, row=0, padx=80, pady=20)

# Botão
botao = Button(janela, text='SORTEAR', command=amigos)
botao.grid(column=0, row=1, padx=80, pady=40)

# Texto_Final
texto_amigos = Label(janela, text='')
texto_amigos.grid(column=0, row=2, padx=80, pady=60)

janela.mainloop()
