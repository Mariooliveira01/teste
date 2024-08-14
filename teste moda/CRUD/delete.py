import sqlite3

#Delete (Exclusão de Produto)
def excluir_produto(produto_id):
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Produtos WHERE id = ?', (produto_id,))
    conn.commit()
    conn.close()