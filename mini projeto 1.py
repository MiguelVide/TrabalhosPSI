conversoes = {
    'A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6',
    'H':'#','I':'1','J':'J','K':'K','L':'1','M':'M','N':'N',
    'O':'0','P':'P','Q':'Q','R':'R','S':'$','T':'7','U':'U',
    'V':'V','W':'W','X':'X','Y':'Y','Z':'2',
    '0':')','1':'!','2':'@','3':'#','4':'$',
    '5':'%','6':'^','7':'&','8':'*','9':'(',' ':'_'
}

while True:
    print("\n--- MENU ---")
    print("1 - Ver lista de conversões")
    print("2 - Introduzir frase e gerar password")
    print("0 - Sair")

    opcao = input("Escolhe uma opção: ").lower()

    if opcao == "1":
        print("\nLista de conversões:")
        for chave, valor in conversoes.items():
            print(f"{chave} -> {valor}")

        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    elif opcao == "2":
        # Utilizador introduz a password
        frase = input("\nIntroduz a password: ")
        confirmar = input("Confirma a password: ")

        if frase != confirmar:
            print("❌ Passwords não coincidem!")
            continue

        print("✅ Password confirmada com sucesso.")

        # Gerar password convertida
        password = ""
        for c in frase:
            c_upper = c.upper()
            if c_upper in conversoes:
                password += conversoes[c_upper]
            else:
                password += c

        print("\nPassword gerada:", password)

        # Avaliação baseada no conteúdo introduzido
        tem_numeros = any(c.isdigit() for c in frase)
        tem_especiais = any(not c.isalnum() and c != " " for c in frase)

        if tem_especiais:
            print("Força da password: MUITO BOA")
        elif tem_numeros:
            print("Força da password: BOA")
        else:
            print("Força da password: MUITO MÁ")

        print("\nA entrar no kuma rp...")

        while True:
            voltar = input("\nEscreve 'menu' para voltar: ").lower()
            if voltar == "menu":
                break

    elif opcao == "0":
        print("\nPrograma terminado.")
        break

    else:
        print("\nOpção inválida.")
