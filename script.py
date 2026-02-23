def moldura(texto):
    print("\n" + "═" * 55)
    print(f"{texto.center(55)}")
    print("═" * 55)


def mostrar_status(saldo, carrinho):
    total_carrinho = 0
    for item in carrinho:
        total_carrinho += item[1]

    print(f" 💰 SALDO: €{saldo:<10} | 🛒 ITENS: {len(carrinho):<3}")
    print(f" 💳 TOTAL NO CARRINHO: €{total_carrinho}")
    print("-" * 55)


def principal():
    # Estrutura: [ID, Nome, Preço, Quantidade]
    stock_gus = (
        [1, "Pistola 9mm", 450, 10],
        [2, "Rifle Assalto", 2500, 5],
        [3, "Escopeta 12ga", 1200, 3],
        [4, "Sniper .50", 8900, 2],
        [5, "Colete Nível 3", 300, 15]
    )

    carrinho = []
    saldo = 0

    while True:
        moldura("AMMU-NATION DO GUS")
        mostrar_status(saldo, carrinho)

        print(" [1] 🛠️  Trabalhar (+€100)")
        print(" [2] 🔫  Ver Catálogo e Comprar")
        print(" [3] 🛒  Ver Carrinho / Remover Item")
        print(" [4] ✅  Finalizar Compra")
        print(" [5] 🚪  Sair")

        opcao = input("\n> Escolha uma opção: ")

        # 1. TRABALHAR
        if opcao == "1":
            saldo += 100
            print("\n✨ salão de beleza : 'Bom trabalho! Aqui tens os teus €100.'")

        # 2. COMPRAR POR NOME E QUANTIDADE
        elif opcao == "2":
            print(f"\n{'PRODUTO':<20} | {'PREÇO':<8} | {'STOCK'}")
            print("-" * 55)
            for item in stock_gus:
                status = f"{item[3]} un." if item[3] > 0 else "🚫 ESGOTADO"
                print(f"{item[1]:<20} | €{item[2]:<7} | {status}")

            nome_busca = input("\nNome do produto (ou ENTER para voltar): ")

            if nome_busca != "":
                achou = False
                for item in stock_gus:
                    if nome_busca.lower() == item[1].lower():
                        achou = True
                        qtd_input = input(f"Quantos(as) '{item[1]}' queres? ")

                        if qtd_input.isdigit() and int(qtd_input) > 0:
                            qtd_pedida = int(qtd_input)

                            if qtd_pedida <= item[3]:
                                for _ in range(qtd_pedida):
                                    carrinho.append((item[1], item[2], item[0]))
                                item[3] -= qtd_pedida
                                print(f"✅ {qtd_pedida}x {item[1]} adicionado(s)!")
                            else:
                                print(f"❌ Gus: 'Não tenho stock suficiente para {qtd_pedida} unidades!'")
                        else:
                            print("Escolha uma opção válida!!")  # Erro na quantidade

                if not achou:
                    print("Escolha uma opção válida!!")  # Erro no nome do produto

        # 3. VER CARRINHO E REMOVER
        elif opcao == "3":
            moldura("CONTEÚDO DO CARRINHO")
            if not carrinho:
                print("O teu carrinho está vazio.")
            else:
                for i, item in enumerate(carrinho):
                    print(f" {i + 1} ➔ {item[0]:<18} | €{item[1]}")

                print("-" * 55)
                remover = input("Digite o nº para remover (ou ENTER para voltar): ")

                if remover != "":
                    if remover.isdigit() and 0 < int(remover) <= len(carrinho):
                        removido = carrinho.pop(int(remover) - 1)
                        for prod in stock_gus:
                            if prod[0] == removido[2]:
                                prod[3] += 1
                        print(f"♻️ {removido[0]} devolvido ao stock.")
                    else:
                        print("Escolha uma opção válida!!")  # Erro na remoção

        # 4. FINALIZAR
        elif opcao == "4":
            total = sum(item[1] for item in carrinho)
            if not carrinho:
                print("⚠️ O carrinho está vazio!")
            elif saldo >= total:
                saldo -= total
                carrinho.clear()
                moldura("🔥 COMPRA REALIZADA!")
                print("Gus: 'Excelente! Faz bom proveito!'")
            else:
                print(f"❌ Saldo insuficiente! Falta €{total - saldo}")

        # 0. SAIR
        elif opcao == "5":
            print("\nGus: 'Até à próxima.'")
            break

        # ERRO PARA OPÇÃO DO MENU INVÁLIDA
        else:
            print("Escolha uma opção válida!!")


if __name__ == "__main__":
    principal()