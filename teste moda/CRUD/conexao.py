import sqlite3

#Criação da função para conectar ao banco de dados
def conectar():
    try:
        global conn
        conn = sqlite3.connect('moda_express.db')
        global cursor
        cursor = conn.cursor()
        print("Conexão com o Banco realizada com sucesso!")
    except sqlite3.Error as erro:
        print("Erro de conexão com o Banco de Dados.")