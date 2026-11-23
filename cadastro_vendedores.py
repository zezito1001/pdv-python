from datetime import datetime
def cadastro_de_vendedores():
    vendedores = {}
    id = 1

    while True:
        adicionar_vendedor = input("Deseja cadastrar algum vendedor (s/n)? ").strip().lower()
        if adicionar_vendedor.strip().lower() in ("sim", "s", ):
            while True:
                nome = input("Informe o nome do vendedor: ").title().strip()
                if not " " in nome:
                    print("Você deve fornecer nome e sobrenome para prosseguir")
                    continue
                elif len(nome) > 30:
                    print("Nome invalido por execesso de caracteres, por favor informe apenas nome e sobrenome")
                    continue
                data_nascimento = input("Informe a data de nascimento do cliente no formato DD/MM/AAAA: ")
                dia, mes, ano = data_nascimento.split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                hoje = datetime.today()
                idade = hoje.year - ano
                if (hoje.month, hoje.day) < (mes, dia):
                    idade -= 1
                endereco = input("Informe o endereço do vendedor: ")
                cpf = input("Informe o CPF do vendedor sem traços ou pontos : ")
                cpf = cpf.replace(".", "").replace("-", "")
                if len(cpf) != 11 or not cpf.isdigit():
                    print("CPF inválido!")
                    continue
                vendedores[f"{id:04d}"] = {"Nome": nome, "Idade": idade, "CPF": cpf, "Endereço": endereco}
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
        print(f"Nome: {dados['Nome']}")
        print(f"Idade: {dados['Idade']}")
        print(f"Endereço: {dados['Endereço']}")
        print(f"CPF: {dados['CPF'][:3]}.{dados['CPF'][3:6]}.{dados['CPF'][6:9]}-{dados['CPF'][9:]}")
        print(f"ID: VD{id}")
        print("=" * 20)
if __name__ == "__main__":
    vendedores = cadastro_de_vendedores()
    mostrar_vendedores(vendedores)
