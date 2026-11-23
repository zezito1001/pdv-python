from datetime import datetime
def cadastro_cliente():
      cliente = {}
      id = 1
      

      while True:
            cadastro = input("Deseja Cadastrar o cliente? (s/n) ").strip().lower()
            if cadastro.strip().lower() in ("sim", "s"):

                  while True:
                        nome = input("Informe o nome do cliente: ").title().strip()
                        if len(nome) < 15:
                              print("Nome invalido por falta de caracteres, por favor coloque um nome maior ")
                              continue
                        elif len(nome) > 30:
                              print("Nome invalido por execesso de caracteres, por favor informe um nome menor ")
                              continue
                        data_nascimento = input("Informe a data de nascimento do cliente: ")
                        dia, mes, ano = data_nascimento.split("/")
                        dia = int(dia)
                        mes = int(mes)
                        ano = int(ano)
                        hoje = datetime.today()
                        idade = hoje.year - ano                        
                        if (hoje.month, hoje.day) < (mes, dia):                       
                              idade -= 1
                        endereco = input("Informe o endereço do cliente: ").strip().lower().capitalize()
                        cpf = input("Informe o CPF do cliente sem traços ou pontos : ")
                        cpf = cpf.replace(".", "").replace("-", "")
                        if len(cpf) != 11 or not cpf.isdigit():
                              print("CPF inválido!")
                              continue
                        cliente[f"{id:04d}"] = {"Nome": nome, "Idade": idade, "CPF": cpf, "Endereço": endereco }
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
            print(f"Nome: {dados['Nome']}")
            print(f"Idade: {dados['Idade']}")
            print(f"CPF: {dados['CPF'][:3]}.{dados['CPF'][3:6]}.{dados['CPF'][6:9]}-{dados['CPF'][9:]}")
            print(f"Endereço: {dados['Endereço']}")
            print(f"ID: CL{id}")
            print("=" * 20)
if __name__ == "__main__":
      cliente = cadastro_cliente()
      mostrar_cliente(cliente)
