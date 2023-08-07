import sqlite3
from BD.Biblioteca.Interface import *
from time import sleep


def opc(*nome):
    for n in nome:
        print(n)
    linha()
    while True:
        try:
            escolha = int(input('Opção: '))
            linha()
        except TypeError:
            print(f'Erro: Por Favor, digite uma opção! ')
            linha()
        except ValueError:
            print(f'Erro: Por Favor, escolha uma opção válida! ')
            linha()
        except KeyboardInterrupt:
            print('O Usuário prefiriu não informar a opção!')
            linha()
            titulo('Finalizarei o programa... Volte Sempre!')
            break
        else:
            if escolha == 1:
                try:
                    name = str(input('Nome do Banco de Dados: '))
                    if name == '':
                        while name == '':
                            print('Por Favor, insira um nome para o Novo Banco!')
                            name = str(input('Nome do Banco: '))
                except (TypeError, ValueError):
                    print(f'Desculpe! Encontramos um erro!')
                else:
                    conexao = sqlite3.connect(f'{name}.db')

                    cursor = conexao.cursor()

                    cursor.execute("CREATE TABLE clientes(Nome text, Idade integer, Email text)")
                    while True:
                        nomes = str(input('Nome: '))
                        idade = int(input('Idade: '))
                        email = input('Email: ')
                        cursor.execute(f"INSERT INTO clientes VALUES ('"+Nome+"', "+str(Idade)+", '"+Email"')")
                        conexao.commit()
                        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
                        if continuar in 'N':
                            break

            if escolha == 3:
                conexao = sqlite3.connect('Clientes.db')

                cursor = conexao.cursor()

                cursor.execute("SELECT * FROM Clientes")

                print(cursor.fetchall())

            if escolha == 4:
                titulo('Finalizando... Até Logo!')
                sleep(2)
                break
