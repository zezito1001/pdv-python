def cadastro_cliente():
        cliente = {}
        id = 1

        while True:

            cadastro = input("Deseja Cadastrar o cliente ? ").strip().lower()

            if cadastro.strip().lower() in ("sim", "s"):

                while True:

                        nome_cliente = input("Informe o nome do cliente: ")

                        idade_cliente = int(input("Informe a idade do cliente: "))

                        cpf_cliente = input("Informe o CPF do cliente: ")

                        cliente[f"VD{id:03d}"] = {"Nome": nome_cliente, "Idade": idade_cliente, "CPF": cpf_cliente}

                        id+=1

                        while True:
                              add = input("Deseja cadastrar mais clientes ?").strip().lower()

                              if add.strip().lower() in ("sim", "s", "não", "nao"):
                                    break
                              
                              print("Não entendi, poderia informar novamente ? ")

                        if add.strip().lower() in ("não", "nao"):
                              print("Saindo...")
                              break
                break 

            elif cadastro.strip().lower() in ("não", "nao"):
                  print("Saindo...")
                  break
            else:
                  print("Não entendi, poderia me informar novamente ? ")

        return cliente

def mostrar_cliente(cliente):
      for id, dados in cliente.items():

            print(f"Nome: {dados['Nome']}")

            print(f"Idade: {dados['Idade']}")

            print(f"CPF: {dados['CPF']}")

            print(f"ID: {id}")

cliente = cadastro_cliente()
mostrar_cliente(cliente)
