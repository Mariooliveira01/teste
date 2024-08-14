import sqlite3
import delete
from conexao import conectar 
from insert import cadastrar_produto, registrar_venda
def menu_principal():
    while True:
        print("\n--- Sistema de Gerenciamento de Estoque e Vendas ---")
        print("1. Cadastrar Produto")
        print("2. Registrar Venda")
        print("3. Consultar Estoque")
        print("4. Consultar Vendas")
        print("5. Gerar Relatório de Vendas")
        print("6. Atualizar Produto")
        print("7. Excluir Produto")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            produto = cadastrar_produto(nome, quantidade, preco)
            produto.salvarProduto()
            print("Produto cadastrado com sucesso!")
        
        elif escolha == "2":
            produto_id = int(input("ID do Produto: "))
            quantidade = int(input("Quantidade: "))
            conn = sqlite3.connect('moda_express.db')
            cursor = conn.cursor()
            cursor.execute('SELECT preco FROM Produtos WHERE id = ?', (produto_id,))
            preco = cursor.fetchone()[0]
            valor_total = quantidade * preco
            venda = registrar_venda()
            registrar_venda()
            print("Venda registrada com sucesso!")

        elif escolha == "3":
            produtos = Produto.Produto.consultarProduto()
            for prod in produtos:
                print(f"ID: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço: R${prod[3]:.2f}")

        elif escolha == "4":
            vendas = conexao.Venda.consultarVenda()
            for venda in vendas:
                print(f"ID: {venda[0]}, Produto ID: {venda[1]}, Quantidade: {venda[2]}, Data: {venda[3]}, Valor Total: R${venda[4]:.2f}")

        elif escolha == "5":
            relatorio = gerar_relatorio_vendas()
            for item in relatorio:
                print(f"Venda ID: {item[0]}, Produto: {item[1]}, Quantidade: {item[2]}, Data: {item[3]}, Valor Total: R${item[4]:.2f}")

        elif escolha == "6":
            id = int(input("ID do Produto: "))
            quantidade = int(input("Nova Quantidade: "))
            preco = float(input("Novo Preço: "))
            Produto.Produto.atualizarProduto(id, quantidade, preco)
            print("Produto atualizado com sucesso!")

        elif escolha == "7":
            id = int(input("ID do Produto: "))
            delete.excluir_produto(id)
            print("Produto excluído com sucesso!")

        elif escolha == "8":
            break

        else:
            print("Opção inválida. Tente novamente.")

menu_principal()