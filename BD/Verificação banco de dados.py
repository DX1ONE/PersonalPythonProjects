import sqlite3

conexao = sqlite3.connect('Teste.db')

cursor = conexao.cursor()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())