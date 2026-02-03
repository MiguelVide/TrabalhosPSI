# Dicionário que define como cada letra, número ou espaço será convertido
# A chave é o caractere original e o valor é o símbolo correspondente
conversoes = {
    'A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6','H':'#',
    'I':'1','J':'J','K':'K','L':'1','M':'M','N':'N','O':'0','P':'P',
    'Q':'Q','R':'R','S':'$','T':'7','U':'U','V':'V','W':'W','X':'X',
    'Y':'Y','Z':'2',
    '0':')','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^',
    '7':'&','8':'*','9':'(',
    ' ':'_'  # O espaço é convertido no símbolo _
}

# Lista para guardar todas as passwords geradas
historico_passwords = []

# Ciclo infinito que mantém o programa a correr até o utilizador sair
while True:

    # Mostra o menu principal
    print("\n--- MENU ---")
    print("1 - Ver lista de conversões")
    print("2 - Introduzir frase e gerar password")
    print("3 - Ver histórico de passwords")
    print("0 - Sair")

    # Lê a opção do utilizador
    # .lower() evita problemas com maiúsculas/minúsculas
    opcao = input("Escolhe uma opção: ").lower()

    # ================= OPÇÃO 1 =================
    # Mostrar a lista de conversões
    if opcao == "1":

        # Título da lista
        print("\nLista de conversões:")

        # Percorre o dicionário mostrando cada conversão
        for chave, valor in conversoes.items():
            print(chave, "->", valor)

        # Ciclo que obriga o utilizador a escrever "menu" para voltar
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break  # Volta ao menu principal

    # ================= OPÇÃO 2 =================
    # Gerar password a partir de uma frase
    elif opcao == "2":

        # Pede a frase/password ao utilizador
        frase = input("\nIntroduz a password: ")

        # Pede confirmação da password
        confirmar = input("Confirma a password: ")

        # Verifica se as duas passwords são iguais
        if frase != confirmar:
            print("❌ Passwords não coincidem!")
            continue  # Volta ao menu principal

        # Mensagem de sucesso
        print("✅ Password confirmada com sucesso.")

        # Variável onde será construída a password convertida
        password = ""

        # Percorre cada caractere da frase original
        for c in frase:

            # Converte o caractere para maiúscula
            c_upper = c.upper()

            # Se o caractere existir no dicionário de conversões
            if c_upper in conversoes:
                # Adiciona o símbolo correspondente à password
                password += conversoes[c_upper]
            else:
                # Caso não exista conversão, mantém o caractere original
                password += c

        # Mostra a password final gerada
        print("\nPassword gerada:", password)

        # Guarda a password no histórico
        historico_passwords.append(password)

        # -----------------------------
        # VERIFICAÇÃO DA FORÇA DA PASSWORD
        # -----------------------------

        # Variável que indica se a frase tem números
        tem_numeros = False

        # Variável que indica se a frase tem caracteres especiais
        tem_especiais = False

        # Percorre cada caractere da frase original
        for c in frase:

            # Se o caractere for um número
            if c.isdigit():
                tem_numeros = True

            # Se não for letra nem número e não for espaço
            if not c.isalnum() and c != " ":
                tem_especiais = True

        # Avalia a força da password
        if tem_especiais:
            print("Força da password: MUITO BOA")
        elif tem_numeros:
            print("Força da password: BOA")
        else:
            print("Força da password: MUITO MÁ")

        # Mensagem decorativa
        print("\nA entrar no kuma rp...")

        # Aguarda o utilizador escrever "menu"
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    # ================= OPÇÃO 3 =================
    # Mostrar o histórico de passwords
    elif opcao == "3":

        # Título do histórico
        print("\n--- HISTÓRICO DE PASSWORDS ---")

        # Se ainda não houver passwords guardadas
        if len(historico_passwords) == 0:
            print("Ainda não foram geradas passwords.")
        else:
            # Percorre o histórico e mostra cada password numerada
            for i in range(len(historico_passwords)):
                print(i + 1, "-", historico_passwords[i])

        # Aguarda o utilizador escrever "menu"
        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    # ================= OPÇÃO 0 =================
    # Sair do programa
    elif opcao == "0":
        print("\nSaiste do malta rp .")
        break  # Termina o ciclo principal e o programa

    # ================= OPÇÃO INVÁLIDA =================
    # Caso o utilizador escolha uma opção que não existe
    else:
        print("\nOpção inválida.")
