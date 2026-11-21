def cadastro_cliente():
      cliente = {}
      id = 1
      

      while True:
            cadastro = input("Deseja Cadastrar o cliente? (s/n) ").strip().lower()
            if cadastro.strip().lower() in ("sim", "s"):

                  while True:
                        nome = input("Informe o nome do cliente: ").capitalize()
                        data_nascimento = int(input("Informeo ano de nascimento: "))
                        idade = 2026 - data_nascimento
                        cpf = input("Informe o CPF do cliente: ")
                        cliente[f"{id:03d}"] = {"nome": nome, "idade": idade, "CPF": cpf}
                        id += 1

                        while True:
                              add = input("Deseja cadastrar mais clientes? (s/n) ").strip().lower()
                              if add.strip().lower() in ("sim", "s", "não", "nao", "n"):
                                    break
                              print("Não entendi, poderia informar novamente ? ")
                        if add.strip().lower() in ("não", "nao", "n"):
                              print("Saindo...")
                              break
                  break 
            elif cadastro.strip().lower() in ("não", "nao", "n"):
                  print("Saindo...")
                  break
            else:
                  print("Não entendi, poderia me informar novamente ? ")
      return cliente

      
def mostrar_cliente(cliente):
      print("=" * 20)
      for id, dados in cliente.items():
            print(f"nome: {dados['nome']}")
            print(f"idade: {dados['idade']}")
            print(f"CPF: {dados['CPF']}")
            print(f"ID: CL{id}")
if __name__ == "__main__":
      cliente = cadastro_cliente()
      mostrar_cliente(cliente)