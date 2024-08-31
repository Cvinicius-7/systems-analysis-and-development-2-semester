#TP1 Lista de tarefas

#definição de variáveis
tarefas_pendentes = []
tarefas_concluidas = []
tarefa_id = 0

def gerar_id():
    """ Gera um id para a tarefa

    Returns:
        Retorna o id único gerado para a tarefa
    """
    global tarefa_id
    tarefa_id += 1
    return tarefa_id

def adicionar_tarefa(titulo, descricao):
    """Adiciona uma nova tarefa à lista de tarefas pendentes.

    Args:
        titulo (str): O título da tarefa.
        descricao (str): A descrição detalhada da tarefa.

    Returns:
        dict: O dicionário que representa a tarefa adicionada.
    """
    tarefa = {
        'id': gerar_id(),
        'titulo': titulo,
        'descricao': descricao,
        'status': 'pendente'
    }
    tarefas_pendentes.append(tarefa)
    return tarefa

def listar_tarefas(tarefas):
    """Lista todas as tarefas de uma lista fornecida.

    Args:
        tarefas (list): A lista de tarefas a ser listada.

    Returns:
        list: A lista de tarefas fornecida.
    """
    for tarefa in tarefas:
        print(f"\nID: {tarefa['id']} - Título: {tarefa['titulo']}\n Descrição: {tarefa['descricao']} - Status: {tarefa['status']}")
    if not tarefas:
        print("Nenhuma tarefa encontrada")
        return tarefas

def concluir_tarefa(id_tarefa):
    """Marca uma tarefa específica como concluída e move para a lista de tarefas concluídas.
    
    Args:
        id_tarefa (int): O ID da tarefa a ser concluída.

    Returns:
        dict: O dicionário que representa a tarefa concluída, ou None se a tarefa não for encontrada.
    """
    for tarefa in tarefas_pendentes:
        if tarefa['id'] == id_tarefa:
            tarefa['status'] = 'concluida'
            tarefas_concluidas.append(tarefa)
            tarefas_pendentes.remove(tarefa)
            return tarefa
    return None


def menu():
    """ Exibe um menu interativo para o usuário e lida com as opções selecionadas.
    
    O menu permite ao usuário adicionar tarefas, listar tarefas pendentes e concluídas, 
    e concluir tarefas. O loop continua até que o usuário escolha sair.
    """
    while True:
        # Exibe o menu de tarefas
        print("\nMenu de tarefas\n")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas pendentes")
        print("3 - Listar tarefas concluídas")
        print("4 - Concluir tarefa")
        print("0 - Sair")
        
        # Solicita ao usuário que escolha uma opção
        opcao = input("Digite a opção desejada: ")
        
        # Verifica a opção escolhida pelo usuário
        if opcao == '0':
            print("Saindo...")
            # Encerra o programa
            break
        elif opcao == '1':
            # Solicita ao usuário que insira o título e a descrição da tarefa
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(titulo, descricao)
        elif opcao == '2':
            # Lista as tarefas pendentes
            listar_tarefas(tarefas_pendentes)
        elif opcao == '3':
            # Lista as tarefas concluídas
            listar_tarefas(tarefas_concluidas)
        elif opcao == '4':
            # Conclui uma tarefa
            id_tarefa = int(input("Digite o id da tarefa que deseja concluir: "))
            tarefa = concluir_tarefa(id_tarefa)
            if tarefa:
                # Exibe uma mensagem de confirmação
                print(f"Tarefa {tarefa['titulo']} concluída com sucesso!")
            else:
                # Exibe uma mensagem de erro se a tarefa não for encontrada
                print("Tarefa não encontrada")
        else:
            # Exibe uma mensagem de erro se a opção for inválida
            print("Opção inválida")
            
# Inicia o programa 
menu()
   
    
