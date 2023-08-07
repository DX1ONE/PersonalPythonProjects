from  tkinter import *
janela = Tk()

def func():
    if var_azul.get() == 1:
        l1['text'] = 'Azul'
    else:
        l1['text'] = ''
    if var_braco.get() == 1:
        l2['text'] = 'Branco'
    else:
        l2['text'] = ''
    if var_vermelho.get() == 1:
        l3['text'] = 'Vermelho'
    else:
        l3['text'] = ''
    if var_amarelo.get() == 1:
        l4['text'] = 'Amarelo'
    else:
        l4['text'] = ''

l1 = Label(janela, text='', font='Arial 22', background='light blue', foreground='blue')
l1.place(x=200, y=50 )
l2 = Label(janela, text='', font='Arial 22', background='light blue', foreground='white')
l2.place(x=290, y=50)
l3 = Label(janela, text='', font='Arial 22', background='light blue', foreground='red')
l3.place(x=400, y=50)
l4 = Label(janela, text='', font='Arial 22', background='light blue', foreground='yellow')
l4.place(x=550, y=50)


var_azul = IntVar()
Checkbutton(janela, text='Azul', background='light blue', variable= var_azul).place(x=300, y=200)
var_braco = IntVar()
Checkbutton(janela, text='Branco', background='light blue', variable= var_braco).place(x=300, y=230)
var_vermelho = IntVar()
Checkbutton(janela, text='Vermelho', background='light blue', variable= var_vermelho).place(x=300, y=260)
var_amarelo = IntVar()
Checkbutton(janela, text='Amarelo', background='light blue', variable=var_amarelo).place(x=300, y=290)

Button(janela, text='Clique', command=func, background='yellow').place(x=310, y=350)


janela.geometry('900x600+0+0')
janela.configure(background='light blue')
janela.mainloop()
