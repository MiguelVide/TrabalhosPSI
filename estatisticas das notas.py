# Ciclo infinito para pedir a quantidade de notas até ser válida
while True:
    # Ler do utilizador quantas notas quer inserir
    quantidade = input("Quantas notas quer inserir? ")

    # Verificar se a quantidade é um número inteiro positivo
    if quantidade.isdigit() and int(quantidade) > 0:
        # Converter a quantidade para inteiro
        quantidade = int(quantidade)
        # Sair do ciclo porque o valor é válido
        break
    else:
        # Mensagem de erro se o valor for inválido
        print("Opção inválida, tente novamente")

# Criar uma lista vazia para guardar todas as notas
notas = []

# Ciclo que se repete de acordo com a quantidade de notas
for i in range(quantidade):
    # Ciclo infinito até a nota inserida ser válida
    while True:
        # Pedir a nota ao utilizador
        nota = input(f"Insira a nota {i + 1}: ")

        # Substituir vírgula por ponto para permitir números decimais
        nota = nota.replace(",", ".")

        # Verificar se a nota é um número válido
        if nota.replace(".", "", 1).isdigit():
            # Converter a nota para float
            nota = float(nota)

            # Verificar se a nota está entre 0 e 20
            if 0 <= nota <= 20:
                # Adicionar a nota à lista
                notas.append(nota)
                # Sair do ciclo porque a nota é válida
                break
            else:
                # Mensagem de erro se a nota estiver fora do intervalo
                print("Opção inválida, tente novamente")
        else:
            # Mensagem de erro se não for um número
            print("Opção inválida, tente novamente")

# Calcular a nota mais alta da lista
nota_max = max(notas)

# Calcular a nota mais baixa da lista
nota_min = min(notas)

# Calcular a média das notas
media = sum(notas) / len(notas)

# Mostrar todas as notas inseridas
print("\nNotas inseridas:", notas)

# Mostrar a nota mais alta
print("Nota mais alta:", nota_max)

# Mostrar a nota mais baixa
print("Nota mais baixa:", nota_min)

# Mostrar a média das notas
print("Média:", media)
