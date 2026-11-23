from cadastro_cliente import cadastro_cliente, mostrar_cliente
from cadastro_produto import cadastro_produto, mostrar_produto
from cadastro_vendedores import cadastro_de_vendedores, mostrar_vendedores
from vendas import realizar_venda
from time import sleep

def main():
    clientes = {}
    vendedores = {}
    produtos = {}
    vendas = []
    while True:
        print("\n===================== MENU PDV =======================")
        print("1 - Menu de cadastro           4 - Mostrar vendedores")
        print("2 - Realizar venda             5 - Mostrar produtos")
        print("3 - Mostrar clientes           6 - Consultar vendas")
        print("                     0 - Sair\n")
        opcao_pdv  = int(input("O que gostaria de fazer: "))
        
        if opcao_pdv == 1: 
            while True:
                print("\n========== MENU DE CADASTRO ==========")
                print("1 - Cadastro de clientes")
                print("2 - Cadastro de vendedores")
                print("3 - Cadastro de produto")
                print("0 - Sair do menu de cadastro\n")
                opcao_cadastro = int(input("Tipo de cadastro desejado: "))
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
            if not clientes:
                print("Nenhum cliente cadastrado", end="", flush=True)
                for ponto in range(3):
                    sleep(0.5)
                    print(".", end="", flush=True)
                sleep(0.5)
                print("")
            else:
                mostrar_cliente(clientes)
                sleep(0.5)
        elif opcao_pdv == 4:
            if not vendedores:
                print("Nenhum vendedor cadastrado", end="", flush=True)
                for ponto in range(3):
                    sleep(0.5)
                    print(".", end="", flush=True)
                sleep(0.5)
                print("")
            else:
                mostrar_vendedores(vendedores)
                sleep(0.5)
        elif opcao_pdv == 5:
            if not produtos:
                print("Nenhum produto cadastrado", end="", flush=True)
                for ponto in range(3):
                    sleep(0.5)
                    print(".", end="", flush=True)
                sleep(0.5)
                print("")
            else:
                mostrar_produto(produtos)
                sleep(0.5)
        elif opcao_pdv == 6:
            if not vendas:
                print("Nenhuma venda realizada", end="", flush=True)
                for ponto in range(3):
                    sleep(0.5)
                    print(".", end="", flush=True)
                sleep(0.5)
                print("")
            #else:
                #lógica de recibo/relatório
        elif opcao_pdv == 0:
            print("Encerrando PDV.")
            break
        else:
            print("Opção inválida.")
        


if __name__ == "__main__":
    main()
