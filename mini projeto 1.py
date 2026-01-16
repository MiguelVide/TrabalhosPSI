# Dicionário que define como cada caractere será convertido
conversoes = {
    'A':'@',  # Converte a letra A para @
    'B':'8',  # Converte a letra B para 8
    'C':'(',  # Converte a letra C para (
    'D':'D',  # Mantém a letra D igual
    'E':'3',  # Converte a letra E para 3
    'F':'F',  # Mantém a letra F igual
    'G':'6',  # Converte a letra G para 6
    'H':'#',  # Converte a letra H para #
    'I':'1',  # Converte a letra I para 1
    'J':'J',  # Mantém a letra J igual
    'K':'K',  # Mantém a letra K igual
    'L':'1',  # Converte a letra L para 1
    'M':'M',  # Mantém a letra M igual
    'N':'N',  # Mantém a letra N igual
    'O':'0',  # Converte a letra O para 0
    'P':'P',  # Mantém a letra P igual
    'Q':'Q',  # Mantém a letra Q igual
    'R':'R',  # Mantém a letra R igual
    'S':'$',  # Converte a letra S para $
    'T':'7',  # Converte a letra T para 7
    'U':'U',  # Mantém a letra U igual
    'V':'V',  # Mantém a letra V igual
    'W':'W',  # Mantém a letra W igual
    'X':'X',  # Mantém a letra X igual
    'Y':'Y',  # Mantém a letra Y igual
    'Z':'2',  # Converte a letra Z para 2
    '0':')',  # Converte o número 0 para )
    '1':'!',  # Converte o número 1 para !
    '2':'@',  # Converte o número 2 para @
    '3':'#',  # Converte o número 3 para #
    '4':'$',  # Converte o número 4 para $
    '5':'%',  # Converte o número 5 para %
    '6':'^',  # Converte o número 6 para ^
    '7':'&',  # Converte o número 7 para &
    '8':'*',  # Converte o número 8 para *
    '9':'(',  # Converte o número 9 para (
    ' ':'_'   # Converte espaços para _
}

# Loop principal do programa, executa até o utilizador escolher sair
while True:
    print("\n--- MENU ---")  # Mostra o título do menu
    print("1 - Ver lista de conversões")  # Opção para ver o dicionário
    print("2 - Introduzir frase e gerar password")  # Opção para gerar password
    print("0 - Sair")  # Opção para terminar o programa

    opcao = input("Escolhe uma opção: ").lower()  # Lê a opção e converte para minúsculas

    if opcao == "1":  # Se o utilizador escolher ver as conversões
        print("\nLista de conversões:")  # Título da lista

        for chave, valor in conversoes.items():  # Percorre todas as conversões
            print(f"{chave} -> {valor}")  # Mostra cada conversão individual

        while True:  # Loop para aguardar retorno ao menu
            voltar = input("\nEscreve 'menu' para voltar: ").lower()  # Pede confirmação
            if voltar == "menu":  # Se o utilizador escrever menu
                break  # Sai do loop e volta ao menu principal

    elif opcao == "2":  # Se o utilizador escolher gerar password
        frase = input("\nIntroduz a password: ")  # Pede a password original
        confirmar = input("Confirma a password: ")  # Pede confirmação da password

        if frase != confirmar:  # Verifica se as duas passwords são diferentes
            print("❌ Passwords não coincidem!")  # Mensagem de erro
            continue  # Volta ao início do menu

        print("✅ Password confirmada com sucesso.")  # Confirmação de sucesso

        password = ""  # Variável onde será guardada a password convertida

        for c in frase:  # Percorre cada caractere da frase
            c_upper = c.upper()  # Converte o caractere para maiúscula
            if c_upper in conversoes:  # Verifica se existe no dicionário
                password += conversoes[c_upper]  # Adiciona a conversão
            else:
                password += c  # Mantém o caractere original se não existir conversão

        print("\nPassword gerada:", password)  # Mostra a password final

        tem_numeros = any(c.isdigit() for c in frase)
        # Verifica se a frase original contém pelo menos um número

        tem_especiais = any(not c.isalnum() and c != " " for c in frase)
        # Verifica se contém caracteres especiais (exceto espaço)

        if tem_especiais:  # Se tiver caracteres especiais
            print("Força da password: MUITO BOA")
        elif tem_numeros:  # Se tiver apenas números
            print("Força da password: BOA")
        else:  # Se não tiver números nem especiais
            print("Força da password: MUITO MÁ")

        print("\nA entrar no kuma rp...")  # Mensagem decorativa

        while True:  # Loop para voltar ao menu
            voltar = input("\nEscreve 'menu' para voltar: ").lower()  # Pede confirmação
            if voltar == "menu":  # Se o utilizador escrever menu
                break  # Sai do loop

    elif opcao == "0":  # Se o utilizador escolher sair
        print("\nPrograma terminado.")  # Mensagem final
        break  # Termina o loop principal

    else:  # Caso a opção não seja válida
        print("\nOpção inválida.")  # Mensagem de erro
