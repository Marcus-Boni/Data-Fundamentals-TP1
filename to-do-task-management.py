from datetime import datetime

tarefas = []

def adicionar_tarefa(descricao, prazo_final, urgencia="Normal"):
    """
    Adiciona uma nova tarefa à lista de tarefas.
    
    Parâmetros:
    - descricao (str): Descrição da tarefa.
    - prazo_final (str): Data limite para a tarefa (formato YYYY-MM-DD).
    - urgencia (str): Nível de urgência da tarefa (opcional; padrão é "Normal").
    """
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "data_criacao": datetime.now().strftime("%Y-%m-%d"),
        "status": "Pendente",
        "prazo_final": prazo_final,
        "urgencia": urgencia
    }
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso.")

def listar_tarefas():
    """
    Exibe todas as tarefas pendentes e concluídas com seus detalhes.
    """
    if not tarefas:
        print("\nNenhuma tarefa encontrada.")
        return
    print("\nLista de Tarefas:")
    for tarefa in tarefas:
        status = "[Concluída]" if tarefa["status"] == "Concluída" else "[Pendente]"
        print(f"\nID: {tarefa['id']} {status}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Criada em: {tarefa['data_criacao']}")
        print(f"Prazo final: {tarefa['prazo_final']}")
        print(f"Urgência: {tarefa['urgencia']}")

def marcar_como_concluida(tarefa_id):
    """
    Marca uma tarefa específica como concluída.
    
    Parâmetros:
    - tarefa_id (int): ID da tarefa a ser marcada como concluída.
    """
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["status"] = "Concluída"
            print("\nTarefa marcada como concluída.")
            return
    print("\nTarefa não encontrada.")

def remover_tarefa(tarefa_id):
    """
    Remove uma tarefa específica da lista de tarefas.
    
    Parâmetros:
    - tarefa_id (int): ID da tarefa a ser removida.
    """
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != tarefa_id]
    print("\nTarefa removida com sucesso.")

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n---- Menu de Gestão de Tarefas ----")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da Tarefa: ")
        prazo_final = input("Prazo Final (YYYY-MM-DD): ")
        urgencia = input("Nível de Urgência (Baixa, Normal, Alta): ")
        adicionar_tarefa(descricao, prazo_final, urgencia)

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        try:
            tarefa_id = int(input("ID da Tarefa para Marcar como Concluída: "))
            marcar_como_concluida(tarefa_id)
        except ValueError:
            print("\nID inválido. Tente novamente.")

    elif opcao == "4":
        try:
            tarefa_id = int(input("ID da Tarefa para Remover: "))
            remover_tarefa(tarefa_id)
        except ValueError:
            print("\nID inválido. Tente novamente.")

    elif opcao == "5":
        print("\nSaindo do sistema. Adeus! TP finalizado.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
