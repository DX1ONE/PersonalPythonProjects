from tkinter import *

def funcao_botao():
    try:
        n1 = int(caixa_l.get())
        n2 = int(caixa2_l.get())

    except ValueError:
        res = 'Preencha os Campos,\npor gentileza!'
    except TypeError:
        res = 'Preencha os Campos com valores válidos!' 
    else:
        res = n1 + n2


    label_l['text'] = 'O Resultado da Soma é: '
    label_l['text'] = label_l['text'] + str(res)



janela = Tk()

label_l = Label(janela, text='O resultado da soma é: ', font='Arial 20')
label_l.place(x=100,y=300)

label2_l = Label(janela, text='+', font='Arial 23')
label2_l.place(x=420, y=100)

caixa_l = Entry(janela, background='red', width=10, font='Arial 30')
caixa_l.place(x=100,y=100)

caixa2_l = Entry(janela, background='red', width=10, font='Arial 30')
caixa2_l.place(x=520,y=100)
botao_1 = Button(janela, width=25, text='Press', command=funcao_botao, background='red')
botao_1.place(x=320,y=200)



janela.geometry('800x600+0+0')
janela.mainloop()