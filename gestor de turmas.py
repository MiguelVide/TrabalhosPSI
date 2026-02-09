import os

# Banco de dados
turmas = {}
mapas_sala = {}  # Armazena a disposição das cadeiras


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner(titulo):
    limpar_tela()
    print("\033[95m" + "█" * 60)
    print(f"\033[1;37m {titulo.center(58)}")
    print("\033[95m" + "█" * 60 + "\033[0m")


def organizar_assentos():
    banner("ORGANIZAR ASSENTOS")
    t = input("Qual a Turma? ").upper().strip()

    if t not in turmas:
        print("\033[91m[!] Turma não existe. Crie a turma primeiro.")
        input("Enter para voltar...")
        return

    # Se a turma não tem mapa, criamos um 5x5 por padrão
    if t not in mapas_sala:
        mapas_sala[t] = [["[ Vazios ]" for _ in range(5)] for _ in range(5)]

    print(f"\nAlunos disponíveis: {', '.join(turmas[t].keys())}")
    nome = input("Nome do aluno para sentar: ").title().strip()

    if nome in turmas[t]:
        try:
            fila = int(input("Fila (0-4): "))
            coluna = int(input("Cadeira (0-4): "))
            mapas_sala[t][fila][coluna] = f"[{nome[:7]}]"  # Corta o nome se for grande
            print(f"\033[92m[✓] {nome} sentado na Fila {fila}, Cadeira {coluna}!")
        except (ValueError, IndexError):
            print("\033[91m[!] Coordenada inválida. Use números de 0 a 4.")
    else:
        print("\033[91m[!] Este aluno não pertence a esta turma.")
    input("\nContinuar...")


def ver_mapa():
    banner("MAPA DA SALA")
    t = input("Ver mapa de qual Turma? ").upper().strip()

    if t in mapas_sala:
        print(f"\n\033[94m   CADERAS DA TURMA {t}:")
        print("      0          1          2          3          4")
        for i, fila in enumerate(mapas_sala[t]):
            linha = "  ".join(f"{item:^10}" for item in fila)
            print(f"\033[1;37m{i} \033[0m {linha}")
    else:
        print("\033[91m[!] Nenhum mapa configurado para esta turma.")
    input("\n\033[95mPressione Enter para sair do mapa...")


def gerenciar_aluno(acao):
    if acao == "adicionar":
        banner("MATRÍCULA DE ALUNO")
        t = input("TURMA: ").upper().strip()
        n = input("NOME DO ALUNO: ").title().strip()
        if t not in turmas: turmas[t] = {}
        turmas[t][n] = []
        input("\n\033[92m[✓] Aluno registrado! Enter...")
    elif acao == "expulsar":
        banner("ZONA DE EXPULSÃO")
        t = input("TURMA: ").upper().strip()
        n = input("NOME PARA REMOVER: ").title().strip()
        if t in turmas and n in turmas[t]:
            del turmas[t][n]
            # Remove também do mapa se estiver lá
            if t in mapas_sala:
                for r in range(5):
                    for c in range(5):
                        if n[:7] in mapas_sala[t][r][c]:
                            mapas_sala[t][r][c] = "[ Vazios ]"
            input("\n\033[91m[!] Aluno removido do sistema e da cadeira. Enter...")


def historico():
    banner("HISTÓRICO E OCORRÊNCIAS")
    n_aluno = input("Nome do Aluno: ").title().strip()
    encontrado = False
    for t, alunos in turmas.items():
        if n_aluno in alunos:
            encontrado = True
            print(f"\n\033[94mTURMA: {t} | ALUNO: {n_aluno}")
            if not alunos[n_aluno]: print("Nenhum registro.")
            for i, msg in enumerate(alunos[n_aluno], 1):
                print(f" {i}. {msg}")
            op = input("\n\033[93m[1] Add Ocorrência | [Enter] Sair: ")
            if op == "1":
                alunos[n_aluno].append(input("Descreva: "))
    if not encontrado: input("\n\033[91m[!] Não localizado.")


# --- LOOP PRINCIPAL ---
while True:
    banner("SISTEMA GESTÃO TURBO v2")
    print("\033[94m[1]\033[0m Matricular Aluno")
    print("\033[94m[2]\033[0m Definir Lugar (Sentar)")
    print("\033[92m[3]\033[0m Ver Mapa da Sala")
    print("\033[94m[4]\033[0m Histórico/Notas")
    print("\033[91m[5]\033[0m EXPULSAR")
    print("\033[90m[0] Sair")

    escolha = input("\n\033[1;37mCOMANDO > \033[0m")

    if escolha == "1":
        gerenciar_aluno("adicionar")
    elif escolha == "2":
        organizar_assentos()
    elif escolha == "3":
        ver_mapa()
    elif escolha == "4":
        historico()
    elif escolha == "5":
        gerenciar_aluno("expulsar")
    elif escolha == "0":
        break