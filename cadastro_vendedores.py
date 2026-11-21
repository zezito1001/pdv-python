def cadastro_de_vendedores():
    vendedores = {}
    id = 1

    while True:
        adicionar_vendedor = input("Deseja cadastrar algum vendedor (s/n)? ").strip().lower()
        if adicionar_vendedor.strip().lower() in ("sim", "s", ):
            while True:
                nome = input("Informe o nome do vendedor: ").capitalize()
                idade = int(input("Informe a idade do vendedor: "))
                cpf = input("Informe o CPF do vendedor: ")
                vendedores[f"{id:03d}"] = {"nome": nome, "idade": idade, "CPF": cpf}
                id += 1

                while True:
                    add = input("Deseja cadastrar mais algum vendedor (s/n)? ").strip().lower()
                    if add.strip().lower() in ("sim", "s", "não", "nao", "n"):
                        break
                    print("Não entendi, poderia me informar novamente?")
                if add.strip().lower() in ("nao", "não", "n"):
                    print("Saindo...")
                    break
            break
        elif adicionar_vendedor.strip().lower() in ("não", "nao", "n"):
            print("Saindo...")
            break
        else:
            print("Eu não entendi, poderia informar novamente?")
    return vendedores

def mostrar_vendedores(vendedores):
    print("=" * 20)
    for id, dados in vendedores.items():
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print(f"CPF: {dados['CPF']}")
        print(f"ID: VD{id}")
if __name__ == "__main__":
    vendedores = cadastro_de_vendedores()
    mostrar_vendedores(vendedores)
