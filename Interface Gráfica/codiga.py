import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacao['text'] = texto


janela = Tk()
janela.title('Cotações Atuais')

# Texto == Label
texto_orientação = Label(janela, text='Clique no Botão para começar!'.center(50))
texto_orientação.grid(column=0, row=0, padx=10, pady=10)

# Botão = Button
botao = Button(janela, text= 'VER COTAÇÕES', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

# Texto = Label 
texto_cotacao = Label(janela, text='')
texto_cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()