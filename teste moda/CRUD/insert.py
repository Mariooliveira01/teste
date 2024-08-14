import sqlite3

#Create (Cadastro de Produto)
def cadastrar_produto(nome, quantidade, preco):
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Produtos (nome, quantidade, preco) VALUES (?, ?, ?)', (nome, quantidade, preco))
    conn.commit()
    conn.close()


#Create (Registro de Vendas)
def registrar_venda(produto_id, quantidade):
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    
    # Obtém o preço do produto
    cursor.execute('SELECT preco FROM Produtos WHERE id = ?', (produto_id,))
    preco = cursor.fetchone()[0]
    
    valor_total = preco * quantidade
    
    # Registra a venda
    cursor.execute('INSERT INTO Vendas (produto_id, quantidade, data, valor_total) VALUES (?, ?, date("now"), ?)', (produto_id, quantidade, valor_total))
    
    # Atualiza o estoque
    cursor.execute('UPDATE Produtos SET quantidade = quantidade - ? WHERE id = ?', (quantidade, produto_id))
    conn.commit()
    conn.close()

def salvar(self):
        conn = sqlite3.connect('moda_express.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Produtos (nome, quantidade, preco) VALUES (?, ?, ?)', (self.nome, self.quantidade, self.preco))
        conn.commit()
        conn.close()