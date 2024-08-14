import sqlite3

#Read (Consulta de Produto)
def consultar_produtos():
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

#Read (Geração de Relátorios de Vendas)
def gerar_relatorio_vendas():
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vendas')
    vendas = cursor.fetchall()
    conn.close()
    return vendas