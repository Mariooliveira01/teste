import sqlite3

def criar_banco():
    conn = sqlite3.connect('moda_express.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,quantidade INTEGER NOT NULL,preco REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Vendas (id INTEGER PRIMARY KEY AUTOINCREMENT,produto_id INTEGER NOT NULL,quantidade INTEGER NOT NULL,data TEXT NOT NULL,valor_total REAL NOT NULL,FOREIGN KEY(produto_id) REFERENCES Produtos(id))''')
    conn.commit()
    conn.close()

criar_banco()