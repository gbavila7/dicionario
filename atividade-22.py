alunos =  {
    "Ávila": {
        "Matemática": [9.2, 9.0],
        "Português": [10.0, 8.0],
        "Geografia": [10.0, 10.0],
        "Física": [10.0, 9.5]
    },
    "Randolfo": {
        "Matemática": [9.0, 9.0],
        "Português": [8.7, 10.0],
        "Geografia": [9.6, 8.0],
        "Física": [8.0, 9.0]
    },
    "Maia": {
        "Matemática": [9.5, 9.2],
        "Português": [8.0, 8.7],
        "Geografia": [9.0, 8.6],
        "Física": [10.0, 9.7]
    },
    "Bombastic": {
        "Matemática": [8.0, 7.7],
        "Português": [7.6, 6.0],
        "Geografia": [7.0, 8.1],
        "Física": [6.0, 7.2]
    },
    "Kidzada": {
        "Matemática": [10.0, 10.0],
        "Português": [8.0, 9.2],
        "Geografia": [9.0, 9.0],
        "Física": [10.0, 8.0]
    }
}

def media_notas():
    for nome, materias in alunos.items():
        print(f"Aluno: {nome}")
        for materia, notas in materias.items():
            media = sum(notas) / len(notas)
            print(f"{materia}: {media}")
            continue

def media_geral():
    quantidades_notas = 0
    soma_total = 0

    for materias in alunos.values():
        for notas in materias.values():
            soma_total += sum(notas)
            quantidades_notas += len(notas)

    media_geral = soma_total / quantidades_notas
    print(f'A média geral é: {media_geral:.2f}')

def melhor_aluno():
    melhor = None
    quantidades_notas = 0
    notas_total = 0
    maior_media = -1

    for nome, materias in alunos.items():
        for notas in materias.values():
            notas_total += sum(notas)
            quantidades_notas += len(notas)
        media = notas_total / quantidades_notas if quantidades_notas else 0
        if media > maior_media:
            media = maior_media
            melhor = nome
        
        return melhor, maior_media
    melhor, media = melhor_aluno()
    print(f"Melhor aluno: {melhor}, com média geral de: {media:.2f}")

def media_materias():
    
    soma_total = 0
    quantidade_notas = 0
    
    for materias in alunos.values():
        for matematica, notas in materias.values():
            soma_total += sum(notas)
            quantidade_notas += len(notas)

    media_matematica = soma_total / quantidade_notas
    print(f'A média geral de matemática é: {media_matematica}')

    for materias in alunos.values():
        for geografia, notas in materias.values():
            soma_total += sum(notas)
            quantidade_notas += len(notas)

    media_geografia = soma_total / quantidade_notas
    print(f'A média geral de matemática é: {media_geografia}')

    for materias in alunos.values():
        for portugues, notas in materias.values():
            soma_total += sum(notas)
            quantidade_notas += len(notas)

    media_portugues = soma_total / quantidade_notas
    print(f'A média geral de matemática é: {media_portugues}')

    for materias in alunos.values():
        for fisica, notas in materias.values():
            soma_total += sum(notas)
            quantidade_notas += len(notas)

    media_fisica = soma_total / quantidade_notas
    print(f'A média geral de matemática é: {media_fisica}')

def atualizacao():
    aluno = input("Digite o nome do aluno que deseja atualizar: ")
    if aluno not in alunos:
        print("Aluno não encontrado.")
        return

    print("Matérias disponíveis:")
    for materia in alunos[aluno]:
        print(materia)

    materia = input("Digite o nome da matéria que deseja atualizar: ")
    if materia not in alunos[aluno]:
        print("Matéria não encontrada.")
        return

    try:
        pos = int(input("Qual nota deseja alterar? (1 ou 2): ")) - 1
        if pos not in [0, 1]:
            print("Posição inválida. Escolha 1 ou 2.")
            return

        nova_nota = float(input("Digite a nova nota: "))
        alunos[aluno][materia][pos] = nova_nota
        print(f"Nota atualizada com sucesso para {aluno} em {materia}. Novas notas: {alunos[aluno][materia]}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
            

def menu():
    while True:
        print("\nMenu:")
        print("1 - Média de matérias")
        print("2 - Média geral de notas")
        print("3 - Melhor Aluno")
        print("4 - Média por Matérias")
        print("5 - Atualizar Notas")  # <- nova opção
        print("6 - Sair")
        opcao = input('Insira uma opção: ')

        if opcao == '1':
            media_notas()
        elif opcao == '2':
            media_geral()
        elif opcao == '3':
            melhor_aluno()
        elif opcao == '4':
            media_materias()
        elif opcao == '5':  # <- chamada da nova função
            atualizacao()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
menu()