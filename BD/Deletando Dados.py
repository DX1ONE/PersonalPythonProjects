import sqlite3
try:
    conexao = sqlite3.connect('Teste.db')

    cursor = conexao.cursor()

    cursor.execute("DELETE from pessoas WHERE idade = 18")

    conexao.commit()
    conexao.close()
    print('Os dados foram removidos com sucesso!!')
except sqlite3.Error as erro:
    print(f'Erro encontrado: {erro.__class__}')