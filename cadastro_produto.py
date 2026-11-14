def cadastro_produto():

    produto = {}
    codigo = 1

    while True:
            p = input("Deseja Cadastrar algum Produto?" ).strip().lower()

            if p.strip().lower() in ("sim"):
                while True:
 
                    nome = input("Digite o nome do produto, que você deseja Adicionar: ")

                    valor = float(input("Digite o valor do produto: "))

                    estoque = int(input("Digite a quantidade que tem no estoque desse produto" ))

                    produto[codigo] = {"nome": nome, "valor": valor, "estoque": estoque }

                    codigo += 1

                    while True: 

                        add = input("Deseja Adicionar Mais algum Poduto ? ").strip().lower()
                        if add in ("sim", "s", "não", "nao"):
                         break
                        print("Eu não entendi, poderia digitar novamente ? ")

                    if add in ("não", "nao"):
                        print("Saindo...")
                        break

                break

            elif p in ("não", "nao"):
                print("Saindo...")
                break
            else:
                print("Eu não entendi, Poderia Digitar novamente ?")
    return produto 

def mostrar_produto(produto):

    for codigo, dados in produto.items():
        print("<<<< PRODUTOS CADASTRADOS >>>>")
 
        print(f"codigo do Produto {codigo}")

        print(f"Nome {dados['nome']}")

        print(f"Valor {dados['valor']:.2f} Reais")

        print(f"Estoque {dados['estoque']}")

produto = cadastro_produto()
mostrar_produto(produto)
