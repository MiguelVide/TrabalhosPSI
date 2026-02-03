# Lista para guardar os nomes das pessoas
nomes = []

# Lista para guardar as idades (cada idade corresponde ao nome da mesma posição)
idades = []

# Ciclo infinito para o menu aparecer sempre até o utilizador sair
while True:

    # Mostrar o menu principal
    print("\n--- Gestor de Nomes ---")
    print("1. Adicionar nomes")
    print("2. Remover nome")
    print("3. Listar nomes")
    print("4. Procurar nome")
    print("5. Sair")

    # Ler a opção escolhida pelo utilizador
    opcao = input("Escolha uma opção: ")

    # ================= OPÇÃO 1 - ADICIONAR NOMES =================
    if opcao == "1":

        # Ciclo para validar a quantidade de nomes (tem de ser número)
        while True:
            quantidade = input("Quantos nomes quer adicionar? ")

            # Verifica se o que foi escrito tem apenas números
            if quantidade.isdigit():
                quantidade = int(quantidade)  # Converte para inteiro
                break  # Sai do ciclo
            else:
                print("Erro: insira apenas números.")

        # Ciclo para adicionar cada pessoa
        for i in range(quantidade):

            # Mostrar o número da pessoa
            print("\nPessoa", i + 1)

            # Ciclo para validar o nome (aceita letras e espaços)
            while True:
                nome = input("Nome completo: ")

                # Remove os espaços e verifica se o resto são apenas letras
                if nome.replace(" ", "").isalpha():
                    break  # Nome válido, sai do ciclo
                else:
                    print("Erro: o nome só pode conter letras e espaços.")

            # Ciclo para validar a idade (tem de ser número)
            while True:
                idade = input("Idade: ")

                # Verifica se a idade tem apenas números
                if idade.isdigit():
                    idade = int(idade)  # Converte para inteiro
                    break  # Sai do ciclo
                else:
                    print("Erro: insira apenas números para a idade.")

            # Guarda o nome na lista de nomes
            nomes.append(nome)

            # Guarda a idade na lista de idades
            idades.append(idade)

    # ================= OPÇÃO 2 - REMOVER NOME =================
    elif opcao == "2":

        # Verifica se não há nomes na lista
        if len(nomes) == 0:
            print("Erro: nenhum nome na lista.")
        else:
            # Pede o nome completo a remover
            nome = input("Nome completo a remover: ")

            # Ciclo para validar a idade
            while True:
                idade = input("Idade da pessoa a remover: ")

                # Verifica se a idade é numérica
                if idade.isdigit():
                    idade = int(idade)
                    break
                else:
                    print("Erro: insira apenas números.")

            # Variável para saber se alguém foi removido
            removido = False

            # Percorre todas as pessoas guardadas
            for i in range(len(nomes)):

                # Verifica se nome e idade coincidem
                if nomes[i] == nome and idades[i] == idade:
                    print("Removido:", nomes[i], "-", idades[i], "anos")

                    # Remove o nome e a idade da mesma posição
                    nomes.pop(i)
                    idades.pop(i)

                    removido = True  # Marca que foi removido
                    break  # Sai do ciclo

            # Se não encontrou ninguém para remover
            if not removido:
                print("Pessoa não encontrada.")

    # ================= OPÇÃO 3 - LISTAR NOMES =================
    elif opcao == "3":

        # Verifica se a lista está vazia
        if len(nomes) == 0:
            print("Lista vazia.")
        else:
            # Percorre todas as pessoas guardadas
            for i in range(len(nomes)):
                print(nomes[i], "-", idades[i], "anos")

    # ================= OPÇÃO 4 - PROCURAR NOME =================
    elif opcao == "4":

        # Verifica se há nomes na lista
        if len(nomes) == 0:
            print("Lista vazia.")
        else:
            # Pede o nome (ou apelido) a procurar
            nome_procurado = input("Nome a procurar: ").lower()

            # Variável para saber se encontrou alguém
            encontrado = False

            # Percorre a lista de nomes
            for i in range(len(nomes)):

                # Divide o nome completo em partes (nome próprio e apelidos)
                partes_nome = nomes[i].lower().split()

                # Verifica se o nome procurado está em alguma parte
                if nome_procurado in partes_nome:
                    print("Encontrado:", nomes[i], "-", idades[i], "anos")
                    encontrado = True

            # Se não encontrou ninguém
            if not encontrado:
                print("Nome não encontrado.")

    # ================= OPÇÃO 5 - SAIR =================
    elif opcao == "5":
        print("A sair...")
        break  # Termina o programa

    # ================= OPÇÃO INVÁLIDA =================
    else:
        print("Opção inválida.")
