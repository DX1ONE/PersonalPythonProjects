from Biblioteca.Opções import *
from Biblioteca.Interface import *
try:
    titulo('BASE DE DADOS')
    opc('1.Criar uma Base ', '2.Inserir Dados', '3.Verificar Dados', '4.Encerrar')
except Exception as erro:
    print(f'Encontramos um erro: {erro.__class__}')
finally:
    print('Volte Sempre!')