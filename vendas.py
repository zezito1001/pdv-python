from datetime import datetime
from time import sleep


def escolher_pessoa(cadastros, tipo):
    print(f"\nSelecione um {tipo}:")
    if tipo == "cliente":
        for codigo, pessoa in cadastros.items():
            print(f"CL{codigo} - {pessoa['nome']}")
    else:
        for codigo, pessoa in cadastros.items():
            print(f"VD{codigo} - {pessoa['nome']}")

    codigo_escolhido = input(f"Código do {tipo}: ").strip().upper()

    if codigo_escolhido not in cadastros:
        print(f"{tipo.capitalize()} não encontrado.")
        return None

    return codigo_escolhido

def realizar_venda(clientes, vendedores, produtos, vendas):
    if not clientes or not vendedores or not produtos:
        print("Cadastre pelo menos um cliente, um vendedor e um produto.")
        sleep(0.8)
        return

    codigo_cliente = escolher_pessoa(clientes, "cliente")
    if codigo_cliente is None:
        return

    codigo_vendedor = escolher_pessoa(vendedores, "vendedor")
    if codigo_vendedor is None:
        return

    carrinho = {}

    while True:
        print("\n========== PRODUTOS ==========")
        for codigo, produto in produtos.items():
            print(
                f"PR{codigo} - {produto['nome']} | "
                f"R$ {produto['valor']:.2f} | "
                f"Estoque: {produto['estoque']}"
            )

        codigo_produto = input("Código do produto (0 para finalizar, C para cancelar): ").strip().upper()

        if codigo_produto == "C":
            print("Venda cancelada.")
            return

        if codigo_produto == "0":
            break

        if codigo_produto not in produtos:
            print("Produto não encontrado.")
            sleep(0.8)
            continue

        quantidade_digitada = input("Quantidade: ").strip()

        if not quantidade_digitada.isdecimal():
            print("Digite uma quantidade inteira positiva.")
            continue

        quantidade = int(quantidade_digitada)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        quantidade_no_carrinho = 0

        if codigo_produto in carrinho:
            quantidade_no_carrinho = carrinho[codigo_produto]["quantidade"]

        estoque_disponivel = (
            produtos[codigo_produto]["estoque"] - quantidade_no_carrinho
        )

        if quantidade > estoque_disponivel:
            print(f"Estoque insuficiente. Disponível: {estoque_disponivel}.")
            sleep(0.8)
            continue

        if codigo_produto in carrinho:
            carrinho[codigo_produto]["quantidade"] += quantidade
        else:
            carrinho[codigo_produto] = {
                "codigo": codigo_produto,
                "nome": produtos[codigo_produto]["nome"],
                "quantidade": quantidade,
                "valor_unitario": produtos[codigo_produto]["valor"],
            }
        print("Adicionando produto ao carrinho", end="", flush=True)
        for ponto in range(3):
            sleep(0.5)
            print(".", end="", flush=True)
        sleep(0.5)
        print("")
    if not carrinho:
        print("Venda não realizada: carrinho vazio.")
        sleep(0.8)
        return

    itens_venda = []
    total_venda = 0

    print("\n========== CARRINHO ==========")
    for item in carrinho.values():
        item["subtotal"] = round(item["quantidade"] * item["valor_unitario"], 2)
        total_venda += item["subtotal"]
        itens_venda.append(item)
        print(f"{item['nome']} x {item['quantidade']} = R$ {item['subtotal']:.2f}")

    total_venda = round(total_venda, 2)
    print(f"Total: R$ {total_venda:.2f}")

    confirmacao = input("Confirmar venda? (s/n): ").strip().lower()

    if confirmacao not in ("s", "sim"):
        print("Venda cancelada. Estoque não alterado.")
        return

    for codigo_produto, item in carrinho.items():
        produtos[codigo_produto]["estoque"] -= item["quantidade"]

    venda = {
        "numero": len(vendas) + 1,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "vendedor": vendedores[codigo_vendedor]["nome"],
        "cliente": clientes[codigo_cliente]["nome"],
        "itens": itens_venda,
        "total": total_venda,
        "comissao": round(total_venda * 0.05, 2),
    }

    vendas.append(venda)
    print("Venda realizada com sucesso.")
