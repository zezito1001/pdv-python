vendedor = {}
id_vendas = 1

while True:

    nome = input("Digite o nome do vendedor (ou Sair): ")

    if(nome.lower() == "sair"):
        print("Saindo...")
        break
    id_formatado = str(id_vendas).zfill(3)

    vendedor[id_formatado]=nome

    id_vendas += 1

    for id_cod, nome_vendedor in vendedor.items():
        print(f"Vendedor: {nome_vendedor} ID: {id_cod}")
        
cliente = {}


while True:

    nome = input("Digite o nome do Cliente(ou Sair): ")

    if(nome.lower() == "sair"):
        print("Saindo...")
        break

    cpf = input("Digite o CPF do Cliente A ser Cadastrado")
    
    cliente[cpf] = nome

for id_cpf, nome_cliente in cliente.items():
    print(f"Cliente: {nome_cliente}  CPF : {id_cpf}")


produto = {}

while True:

    nome = input("Digite o nome do produto(ou Sair)")

    if(nome.lower() == "sair"):
        print("Saindo...")
        break
    preco = float(input("Digite o valor desse produto" ))

    quant_no_estoque = int(input("Digite quanto tem no estoque"))

    produto[nome] = {"preco": preco, "estoque": quant_no_estoque}

for nome_produto, dados in produto.items():
    print(f"Nome do produto: {nome_produto}")
    print(f"Preço do produto: {dados['preco']} reais")
    print(f"Quantidade em estoque: {dados['estoque']}")
    







