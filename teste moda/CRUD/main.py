from criar_banco import criar_banco
from insert import cadastrar_produto, registrar_venda
from read import consultar_produtos, gerar_relatorio_vendas
from update import atualizar_estoque
from delete import excluir_produto


# Criação do banco de dados
criar_banco()

# Cadastro de produtos
cadastrar_produto('Camiseta', 50, 29.90)
cadastrar_produto('Calça Jeans', 30, 79.90)

# Consulta de produtos
produtos = consultar_produtos()
print("Produtos em estoque:")
for produto in produtos:
    print(produto)

# Registro de uma venda
registrar_venda(1, 3)  # Vendendo 3 camisetas

# Geração de relatório de vendas
relatorio = gerar_relatorio_vendas()
print("\nRelatório de vendas:")
for venda in relatorio:
    print(venda)

# Atualização de estoque
atualizar_estoque(1, 45)  # Atualiza o estoque da camiseta para 45 unidades

# Exclusão de um produto
excluir_produto(2)  # Exclui o produto com id 2
