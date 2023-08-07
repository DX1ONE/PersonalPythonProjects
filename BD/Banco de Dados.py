import sqlite3

nome = 'Diogo'
idade = 18
email = 'diogof040@gmail.com'


conexao = sqlite3.connect('Teste.db')

cursor = conexao.cursor()

# cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)")

# cursor.execute("INSERT INTO pessoas VALUES('Maria',40,'maria_123@gmail.com')")

# cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"',"+str(idade)+",'"+email+"')")

cursor.execute("UPDATE pessoas SET nome = 'Cacoio' WHERE idade = 40")

conexao.commit()

