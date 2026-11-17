from cadastro_cliente import cadastro_cliente, mostrar_cliente
from cadastro_produto import cadastro_produto, mostrar_produto
from cadastro_vendedores import cadastro_de_vendedores, mostrar_vendedores
from vendas import realizar_venda


def main():
    print("========== CADASTROS INICIAIS ==========")
    clientes = cadastro_cliente()
    vendedores = cadastro_de_vendedores()
    produtos = cadastro_produto()
    vendas = []

    while True:
        print("\n========== MENU PDV ==========")
        print("1 - Realizar venda")
        print("2 - Mostrar clientes")
        print("3 - Mostrar vendedores")
        print("4 - Mostrar produtos")
        print("5 - Consultar vendas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            realizar_venda(clientes, vendedores, produtos, vendas)
        elif opcao == "2":
            mostrar_cliente(clientes)
        elif opcao == "3":
            mostrar_vendedores(vendedores)
        elif opcao == "4":
            mostrar_produto(produtos)
        elif opcao == "5":
            if not vendas:
                print("Nenhuma venda realizada.")
        elif opcao == "0":
            print("Encerrando PDV.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
