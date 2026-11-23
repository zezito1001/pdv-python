def cadastro_produto():
    produto = {}
    id = 1

    while True:
            p = input("Deseja Cadastrar algum Produto (s/n)? " ).strip().lower()
            if p.strip().lower() in ("sim"):
                while True:
                    nome = input("Digite o nome do produto, que você deseja Adicionar: ").title().strip()
                    valor = input("Digite o valor do produto: ")
                    valor = valor.replace(",", ".")
                    valor = float(valor)
                    estoque = int(input("Digite a quantidade que tem no estoque desse produto: " ))
                    data_de_vencimento = input("Informe a data de validade do produto no formato DD/MM/AAAA: ")
                    dia, mes, ano = data_de_vencimento.split("/")
                    dia = int(dia)
                    mes = int(mes)
                    ano = int(ano)
                    produto[f"{id:04d}"] = {"nome": nome, "valor": valor, "estoque": estoque, "Vencimento": data_de_vencimento }
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

from datetime import date
def mostrar_produto(produto):
    print("<<<< PRODUTOS CADASTRADOS >>>>")
    print("=" * 20)
    for id, dados in produto.items():
        print(f"id do Produto: PR{id}")
        print(f"Nome: {dados['nome']}")
        print(f"Valor: R$ {dados['valor']:.2f}".replace(".", ","))
        print(f"Estoque: {dados['estoque']}")
        print(f"Vencimento: {dados['Vencimento']}")
        dia, mes, ano = dados['Vencimento'].split("/")
        vencimento = date(int(ano), int(mes), int(dia))
        hoje = date.today()

        if vencimento < hoje:
            print("Situação: PRODUTO VENCIDO!")

        elif vencimento == hoje:
            print("Situação: VENCE HOJE!")

        else:
            print("Situação: DENTRO DA VALIDADE!")
        print("=" * 20)

if __name__ == "__main__":
    produto = cadastro_produto()
    mostrar_produto(produto)
