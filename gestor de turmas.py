import os  # Importa o módulo os para permitir comandos do sistema operacional

# -----------------------------
# "Banco de dados" em memória
# -----------------------------

turmas = {}  # Dicionário que armazena as turmas e seus alunos

mapas_sala = {}  # Dicionário que guarda o mapa de cadeiras de cada turma

# -----------------------------
# Funções utilitárias
# -----------------------------

def limpar_tela():  # Função responsável por limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')  # Usa 'cls' no Windows e 'clear' no Linux/Mac


def banner(titulo):  # Função que exibe um cabeçalho estilizado
    limpar_tela()  # Limpa a tela antes de mostrar o banner
    print("\033[95m" + "█" * 60)  # Imprime linha superior colorida
    print(f"\033[1;37m {titulo.center(58)}")  # Mostra o título centralizado
    print("\033[95m" + "█" * 60 + "\033[0m")  # Linha inferior e reset das cores


def pedir_nome(mensagem):  # Função para solicitar e validar nomes
    """
    Solicita um nome e valida:
    - Apenas letras
    - Permite espaços
    """
    while True:  # Loop infinito até o nome ser válido
        nome = input(mensagem).strip()  # Lê o nome e remove espaços extras

        if nome.replace(" ", "").isalpha():  # Verifica se só contém letras
            return nome.title()  # Retorna o nome formatado
        else:
            print("\033[91m[!] Nome inválido. Use apenas letras.\033[0m")  # Erro de validação

# -----------------------------
# Organização dos assentos
# -----------------------------

def organizar_assentos():  # Função para organizar os lugares da sala
    banner("ORGANIZAR ASSENTOS")  # Exibe o banner da seção

    t = input("Qual a Turma? ").upper().strip()  # Solicita a turma

    if t not in turmas:  # Verifica se a turma existe
        print("\033[91m[!] Turma não existe. Crie a turma primeiro.")  # Mensagem de erro
        input("Enter para voltar...")  # Pausa
        return  # Encerra a função

    if t not in mapas_sala:  # Cria o mapa da sala se não existir
        mapas_sala[t] = [["[ Vazios ]" for _ in range(5)] for _ in range(5)]  # Matriz 5x5

    print(f"\nAlunos disponíveis: {', '.join(turmas[t].keys())}")  # Lista alunos

    nome = pedir_nome("Nome do aluno para sentar: ")  # Solicita nome do aluno

    if nome in turmas[t]:  # Verifica se o aluno pertence à turma
        try:
            fila = int(input("Fila (0-4): "))  # Solicita a fila
            coluna = int(input("Cadeira (0-4): "))  # Solicita a coluna

            mapas_sala[t][fila][coluna] = f"[{nome[:7]}]"  # Coloca o aluno na cadeira

            print(f"\033[92m[✓] {nome} sentado na Fila {fila}, Cadeira {coluna}!")  # Confirmação
        except (ValueError, IndexError):  # Captura erros de entrada
            print("\033[91m[!] Coordenada inválida. Use números de 0 a 4.")  # Erro
    else:
        print("\033[91m[!] Este aluno não pertence a esta turma.")  # Aluno inválido

    input("\nContinuar...")  # Pausa

# -----------------------------
# Ver mapa da sala
# -----------------------------

def ver_mapa():  # Função para exibir o mapa da sala
    banner("MAPA DA SALA")  # Exibe o banner

    t = input("Ver mapa de qual Turma? ").upper().strip()  # Solicita turma

    if t in mapas_sala:  # Verifica se existe mapa
        print(f"\n\033[94m   CADERAS DA TURMA {t}:")  # Cabeçalho
        print("      0          1          2          3          4")  # Numeração das colunas

        for i, fila in enumerate(mapas_sala[t]):  # Percorre as filas
            linha = "  ".join(f"{item:^10}" for item in fila)  # Centraliza cadeiras
            print(f"\033[1;37m{i} \033[0m {linha}")  # Exibe a linha
    else:
        print("\033[91m[!] Nenhum mapa configurado para esta turma.")  # Erro

    input("\n\033[95mPressione Enter para sair do mapa...")  # Pausa

# -----------------------------
# Gerenciamento de alunos
# -----------------------------

def gerenciar_aluno(acao):  # Função genérica para adicionar ou expulsar alunos

    if acao == "adicionar":  # Caso seja matrícula
        banner("MATRÍCULA DE ALUNO")  # Banner

        t = input("TURMA: ").upper().strip()  # Solicita turma
        n = pedir_nome("NOME DO ALUNO: ")  # Solicita nome

        if t not in turmas:  # Cria a turma se não existir
            turmas[t] = {}

        turmas[t][n] = []  # Inicializa histórico do aluno

        input("\n\033[92m[✓] Aluno registrado! Enter...")  # Confirmação

    elif acao == "expulsar":  # Caso seja expulsão
        banner("ZONA DE EXPULSÃO")  # Banner

        t = input("TURMA: ").upper().strip()  # Solicita turma
        n = pedir_nome("NOME PARA REMOVER: ")  # Solicita nome

        if t in turmas and n in turmas[t]:  # Verifica existência
            del turmas[t][n]  # Remove o aluno

            if t in mapas_sala:  # Remove do mapa da sala
                for r in range(5):  # Percorre linhas
                    for c in range(5):  # Percorre colunas
                        if n[:7] in mapas_sala[t][r][c]:  # Verifica cadeira
                            mapas_sala[t][r][c] = "[ Vazios ]"  # Libera cadeira

            input("\n\033[91m[!] Aluno removido do sistema e da cadeira. Enter...")  # Confirmação

# -----------------------------
# Histórico
# -----------------------------

def historico():  # Função para visualizar histórico do aluno
    banner("HISTÓRICO E OCORRÊNCIAS")  # Banner

    n_aluno = pedir_nome("Nome do Aluno: ")  # Solicita nome
    encontrado = False  # Flag de controle

    for t, alunos in turmas.items():  # Percorre turmas
        if n_aluno in alunos:  # Verifica se aluno existe
            encontrado = True  # Marca como encontrado
            print(f"\n\033[94mTURMA: {t} | ALUNO: {n_aluno}")  # Cabeçalho

            if not alunos[n_aluno]:  # Verifica histórico vazio
                print("Nenhum registro.")  # Mensagem

            for i, msg in enumerate(alunos[n_aluno], 1):  # Lista ocorrências
                print(f" {i}. {msg}")  # Exibe ocorrência

            op = input("\n\033[93m[1] Add Ocorrência | [Enter] Sair: ")  # Menu
            if op == "1":  # Se escolher adicionar
                alunos[n_aluno].append(input("Descreva: "))  # Adiciona ocorrência

    if not encontrado:  # Caso aluno não exista
        input("\n\033[91m[!] Não localizado.")  # Mensagem

# -----------------------------
# Loop principal
# -----------------------------

while True:  # Loop infinito do programa
    banner("Inovar Dos Sigmas")  # Banner principal

    print("\033[94m[1]\033[0m Matricular Aluno")  # Opção 1
    print("\033[94m[2]\033[0m Definir Lugar (Sentar)")  # Opção 2
    print("\033[92m[3]\033[0m Ver Mapa da Sala")  # Opção 3
    print("\033[94m[4]\033[0m Histórico/Notas")  # Opção 4
    print("\033[91m[5]\033[0m EXPULSAR")  # Opção 5
    print("\033[90m[6] Sair")  # Opção 6

    escolha = input("\n\033[1;37mCOMANDO > \033[0m")  # Lê a escolha

    if escolha == "1":  # Matrícula
        gerenciar_aluno("adicionar")
    elif escolha == "2":  # Organizar assentos
        organizar_assentos()
    elif escolha == "3":  # Ver mapa
        ver_mapa()
    elif escolha == "4":  # Histórico
        historico()
    elif escolha == "5":  # Expulsar
        gerenciar_aluno("expulsar")
    elif escolha == "6":  # Sair
        break  # Encerra o programa
