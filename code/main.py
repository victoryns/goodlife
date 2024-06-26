import datetime

usuarios = []
alimentos = []
atividades = []

def cadastrar_usuario():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    usuario = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "atividades": [],
        "cronograma": []
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!\n")

def cadastrar_alimento():
    nome = input("Nome do alimento: ")
    calorias = int(input("Calorias: "))
    proteinas = float(input("Proteínas (g): "))
    carboidratos = float(input("Carboidratos (g): "))
    gorduras = float(input("Gorduras (g): "))
    alimento = {
        "nome": nome,
        "calorias": calorias,
        "proteinas": proteinas,
        "carboidratos": carboidratos,
        "gorduras": gorduras
    }
    alimentos.append(alimento)
    print(f"Alimento {nome} cadastrado com sucesso!\n")

def cadastrar_atividade():
    nome = input("Nome da atividade: ")
    duracao = int(input("Duração (minutos): "))
    intensidade = input("Intensidade (baixa, média, alta): ")
    atividade = {
        "nome": nome,
        "duracao": duracao,
        "intensidade": intensidade
    }
    atividades.append(atividade)
    print(f"Atividade {nome} cadastrada com sucesso!\n")

def escolher_atividades(usuario):
    print("Escolha as atividades físicas de sua preferência:")
    for i, atividade in enumerate(atividades):
        print(f"{i + 1}. {atividade['nome']} ({atividade['duracao']} min, Intensidade: {atividade['intensidade']})")
    escolha = input("Digite os números das atividades escolhidas separados por vírgula: ")
    indices = [int(x) - 1 for x in escolha.split(",")]
    usuario["atividades"] = [atividades[i] for i in indices]
    print("Atividades escolhidas com sucesso!\n")

def calcular_calorias_diarias(usuario):
    peso = usuario["peso"]
    altura = usuario["altura"]
    idade = usuario["idade"]
    tmb = 10 * peso + 6.25 * altura * 100 - 5 * idade
    return tmb

def montar_cronograma(usuario):
    calorias_diarias = calcular_calorias_diarias(usuario)
    calorias_por_refeicao = calorias_diarias / 3

    refeicoes = ["Café da manhã", "Almoço", "Jantar"]
    cronograma = []

    for refeicao in refeicoes:
        alimentos_escolhidos = []
        calorias_acumuladas = 0

        while calorias_acumuladas < calorias_por_refeicao:
            for alimento in alimentos:
                if calorias_acumuladas + alimento["calorias"] <= calorias_por_refeicao:
                    alimentos_escolhidos.append(alimento)
                    calorias_acumuladas += alimento["calorias"]

        cronograma.append({"refeicao": refeicao, "alimentos": alimentos_escolhidos})

    atividades = usuario["atividades"]
    usuario["cronograma"] = {"refeicoes": cronograma, "atividades": atividades}
    print("Cronograma montado com sucesso!\n")

def visualizar_cronograma(usuario):
    if not usuario["cronograma"]:
        print("Nenhum cronograma encontrado.\n")
        return

    print(f"Cronograma de {usuario['nome']}")
    print("====================")

    print("Refeições:")
    for refeicao in usuario["cronograma"]["refeicoes"]:
        print(f"{refeicao['refeicao']}:")
        for alimento in refeicao["alimentos"]:
            print(f"  - {alimento['nome']} ({alimento['calorias']} calorias)")

    print("\nAtividades:")
    for atividade in usuario["cronograma"]["atividades"]:
        print(f"  - {atividade['nome']} ({atividade['duracao']} min, Intensidade: {atividade['intensidade']})")

    print("====================\n")

def menu():
    while True:
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Alimento")
        print("3. Cadastrar Atividade")
        print("4. Escolher Atividades")
        print("5. Montar Cronograma")
        print("6. Visualizar Cronograma")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            cadastrar_alimento()
        elif escolha == '3':
            cadastrar_atividade()
        elif escolha == '4':
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                for usuario in usuarios:
                    if usuario["nome"] == nome_usuario:
                        escolher_atividades(usuario)
                        break
                else:
                    print("Usuário não encontrado.\n")
            else:
                print("Nenhum usuário cadastrado.\n")
        elif escolha == '5':
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                for usuario in usuarios:
                    if usuario["nome"] == nome_usuario:
                        montar_cronograma(usuario)
                        break
                else:
                    print("Usuário não encontrado.\n")
            else:
                print("Nenhum usuário cadastrado.\n")
        elif escolha == '6':
            if usuarios:
                nome_usuario = input("Digite o nome do usuário: ")
                for usuario in usuarios:
                    if usuario["nome"] == nome_usuario:
                        visualizar_cronograma(usuario)
                        break
                else:
                    print("Usuário não encontrado.\n")
            else:
                print("Nenhum usuário cadastrado.\n")
        elif escolha == '7':
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()