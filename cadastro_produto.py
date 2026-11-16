def cadastro_produto():
    produto = {}
    id = 1

    while True:
            p = input("Deseja Cadastrar algum Produto (s/n)? " ).strip().lower()
            if p.strip().lower() in ("sim"):
                while True:
                    nome = input("Digite o nome do produto, que você deseja Adicionar: ").capitalize()
                    valor = float(input("Digite o valor do produto: "))
                    estoque = int(input("Digite a quantidade que tem no estoque desse produto: " ))
                    produto[f"{id:03d}"] = {"nome": nome, "valor": valor, "estoque": estoque }
                    id += 1

                    while True: 
                        add = input("Deseja adicionar mais algum produto (s/n)? ").strip().lower()
                        if add.strip().lower() in ("sim", "s", "não", "nao", "n"):
                            break
                        print("Eu não entendi, poderia digitar novamente ? ")
                    if add in ("não", "nao", "n"):
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
    print("<<<< PRODUTOS CADASTRADOS >>>>")
    print("=" * 20)
    for id, dados in produto.items():
        print(f"id do Produto: {id}")
        print(f"Nome: {dados['nome']}")
        print(f"Valor: R$ {dados['valor']:.2f}")
        print(f"Estoque: {dados['estoque']}")
        print("=" * 20)

if __name__ == "__main__":
    produto = cadastro_produto()
    mostrar_produto(produto)
