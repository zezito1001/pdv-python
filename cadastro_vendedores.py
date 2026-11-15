def cadastro_de_vendedores():
    vendedores = {}
    id = 1

    while True:

        adicionar_vendedor = input("Deseja cadastrar algum vendedor ? ").strip().lower()

        if adicionar_vendedor.strip().lower() in ("sim", "s", ):

            while True:

                nome = input("Informe o nome do vendedor: ")

                idade = int(input("Informe a idade do vendedor: "))

                cpf = input("Informe o CPF do vendedor: ")

                vendedores[f"VD{id:03d}"] = {"Nome": nome, "Idade": idade, "CPF": cpf }

                id += 1

                while True:
                    add = input("Deseja cadastrar mais algum vendedor ? ").strip().lower()

                    if add.strip().lower() in ("sim", "s", "não", "nao"):
                        break

                    print("Não entendi, poderia me informar novamente ? ")

                if add.strip().lower() in ("não", "nao"):
                    print("Saindo...")
                    break
            break

        elif adicionar_vendedor.strip().lower() in ("não", "nao"):
            print("Saindo...")
            break
        else:
            print("Eu não entendi, poderia informar novamente ? ")
    return vendedores

def mostrar_vendedores(vendedores):
    for id, dados in vendedores.items():

        print(f"Nome: {dados['Nome']}")

        print(f"Idade: {dados['Idade']}")

        print(f"CPF: {dados['CPF']}")

        print(f"ID: {id}")

vendedores = cadastro_de_vendedores()
mostrar_vendedores(vendedores)
        



            
               



                
