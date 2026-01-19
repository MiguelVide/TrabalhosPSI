
# Dicionário que define como cada caractere será convertido
# As chaves são letras/números e os valores são os símbolos correspondentes
conversoes = {
    'A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6','H':'#',
    'I':'1','J':'J','K':'K','L':'1','M':'M','N':'N','O':'0','P':'P',
    'Q':'Q','R':'R','S':'$','T':'7','U':'U','V':'V','W':'W','X':'X',
    'Y':'Y','Z':'2',
    '0':')','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^',
    '7':'&','8':'*','9':'(',
    ' ':'_'  # Espaços são convertidos em _
}

# Lista onde serão guardadas todas as passwords geradas
historico_passwords = []

# Loop principal do programa (executa até o utilizador escolher sair)
while True:
    # Mostra o menu principal
    print("\n--- MENU ---")
    print("1 - Ver lista de conversões")
    print("2 - Introduzir frase e gerar password")
    print("3 - Ver histórico de passwords")
    print("0 - Sair")

    # Lê a opção escolhida pelo utilizador
    # .lower() garante que maiúsculas/minúsculas não fazem diferença
    opcao = input("Escolhe uma opção: ").lower()

    # Opção 1: mostrar todas as conversões
    if opcao == "1":
        print("\nLista de conversões:")
        # Percorre o dicionário e mostra cada conversão
        for chave, valor in conversoes.items():
            print(f"{chave} -> {valor}")

        # Loop para obrigar o utilizador a escrever "menu" para voltar
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    # Opção 2: gerar password
    elif opcao == "2":
        # Pede a password ao utilizador
        frase = input("\nIntroduz a password: ")
        confirmar = input("Confirma a password: ")

        # Verifica se as duas passwords são iguais
        if frase != confirmar:
            print("❌ Passwords não coincidem!")
            continue  # Volta ao menu principal

        print("✅ Password confirmada com sucesso.")

        # Variável onde será construída a password convertida
        password = ""

        # Percorre cada caractere da frase original
        for c in frase:
            c_upper = c.upper()  # Converte para maiúscula
            # Se o caractere existir no dicionário, converte
            if c_upper in conversoes:
                password += conversoes[c_upper]
            else:
                # Se não existir, mantém o caractere original
                password += c

        # Mostra a password final
        print("\nPassword gerada:", password)

        # Guarda a password no histórico
        historico_passwords.append(password)

        # Verifica se a frase original contém números
        tem_numeros = any(c.isdigit() for c in frase)

        # Verifica se contém caracteres especiais (exceto espaço)
        tem_especiais = any(not c.isalnum() and c != " " for c in frase)

        # Avaliação da força da password
        if tem_especiais:
            print("Força da password: MUITO BOA")
        elif tem_numeros:
            print("Força da password: BOA")
        else:
            print("Força da password: MUITO MÁ")

        print("\nA entrar no kuma rp...")

        # Espera até o utilizador escrever "menu"
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    # Opção 3: mostrar histórico de passwords
    elif opcao == "3":
        print("\n--- HISTÓRICO DE PASSWORDS ---")
        # Se o histórico estiver vazio
        if not historico_passwords:
            print("Ainda não foram geradas passwords.")
        else:
            # Mostra todas as passwords guardadas
            for i, p in enumerate(historico_passwords, start=1):
                print(f"{i} - {p}")

        # Aguarda o comando "menu"
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    # Opção 0: sair do programa
    elif opcao == "0":
        print("\nSaiste do malta rp .")
        break  # Termina o loop principal

    # Caso o utilizador escolha uma opção inválida
    else:
        print("\nOpção inválida.")

