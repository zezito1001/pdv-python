from cadastro_cliente import cadastro_cliente, mostrar_cliente
from cadastro_produto import cadastro_produto, mostrar_produto
from cadastro_vendedores import cadastro_de_vendedores, mostrar_vendedores
from vendas import realizar_venda


def main():
    print("========== CADASTROS INICIAIS ==========")
    # clientes = cadastro_cliente()
    # vendedores = cadastro_de_vendedores()
    # produtos = cadastro_produto()
    # vendas = []
    # while True:
    #     print("1 - Cadastro de clientes")
    #     print("2 - Cadastro de vendedores")
    #     print("3 - Cadastro de produto")
    #     opcao_cadastro = int(input("Escolha uma opção: "))
    #     if opcao_cadastro == 1:
    #         clientes = cadastro_cliente()
    #     elif opcao_cadastro == 2:
    #         vendedores = cadastro_de_vendedores()
    #     elif opcao_cadastro == 3:
    #         produtos = cadastro_produto()
    #     elif opcao_cadastro == 0:
    #         break
    #     else:
    #         print("Digite uma opção válida")
    #         continue
    while True:
        print("\n========== MENU PDV ==========")
        print("1 - Menu de cadastro")
        print("2 - Realizar venda")
        print("3 - Mostrar clientes")
        print("4 - Mostrar vendedores")
        print("5 - Mostrar produtos")
        print("6 - Consultar vendas")
        print("0 - Sair\n")
        opcao_pdv  = int(input("Escolha uma opção: "))
        # clientes = cadastro_cliente()
        # vendedores = cadastro_de_vendedores()
        # produtos = cadastro_produto()
        vendas = []
        if opcao_pdv == 1: 
            while True:
                print("\n========== MENU CADASTRO ==========")
                print("1 - Cadastro de clientes")
                print("2 - Cadastro de vendedores")
                print("3 - Cadastro de produto")
                print("0 - Sair do menu de cadastro\n")
                opcao_cadastro = int(input("Escolha uma opção: "))
                if opcao_cadastro == 1:
                    clientes = cadastro_cliente()
                elif opcao_cadastro == 2:
                    vendedores = cadastro_de_vendedores()
                elif opcao_cadastro == 3:
                    produtos = cadastro_produto()
                elif opcao_cadastro == 0:
                    break
                else:
                    print("Digite uma opção válida")
                    continue
        elif opcao_pdv == 2:
            realizar_venda(clientes, vendedores, produtos, vendas)
        elif opcao_pdv == 3:
            mostrar_cliente(clientes)
        elif opcao_pdv == 4:
            mostrar_vendedores(vendedores)
        elif opcao_pdv == 5:
            mostrar_produto(produtos)
        elif opcao_pdv == 6:
            vendas = []
            if not vendas:
                print("Nenhuma venda realizada.")
        elif opcao_pdv == 0:
            print("Encerrando PDV.")
            break
        else:
            print("Opção inválida.")
        


if __name__ == "__main__":
    main()
