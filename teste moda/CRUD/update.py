import sqlite3

#Update (Atualização de Estoque)
def atualizar_estoque(produto_id, nova_quantidade):
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto_id))
    conn.commit()
    conn.close()