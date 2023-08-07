from tkinter import *
janela = Tk()
janela.geometry('500x500')

def funcao1():
    label_l['foreground'] = 'blue'


def funcao2():
    label_l['foreground'] = 'red'


def funcao3():
    label_l['foreground'] = 'green'


def funcao4():
    label_l['foreground'] = 'yellow'


label_l = Label(janela, text='Mude a cor no Menu', font='Arial 25')
label_l.place(x=80, y=150)

m = Menubutton(janela, text='Meu Menu', font='Arial 20', background='white')
m.menu = Menu(m)
m['menu'] = m.menu

m.menu.add_command(label='Azul', command=funcao1)
m.menu.add_command(label='Vermelho', command=funcao2)
m.menu.add_command(label='Verde', command=funcao3)
m.menu.add_command(label='Amarelo', command=funcao4)

m.place(x=180, y=10)
janela.mainloop()