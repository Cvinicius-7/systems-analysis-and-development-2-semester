# Sistema de Controle de Estoque para Loja de Produtos Eletrônicos

#definindo o estoque inicial
estoque_inicial = (
    "Notebook Dell;201;15;3200.00;4500.00#"
    "Notebook Lenovo;202;10;2800.00;4200.00#"
    "Mouse Logitech;203;50;70.00;150.00#"
    "Mouse Razer;204;40;120.00;250.00#"
   "Monitor Samsung;205;10;800.00;1200.00#"
    "Monitor LG;206;8;750.00;1150.00#"
    "Teclado Mecânico Corsair;207;30;180.00;300.00#"
    "Teclado Mecânico Razer;208;25;200.00;350.00#"
    "Impressora HP;209;5;400.00;650.00#"
    "Impressora Epson;210;3;450.00;700.00#"
    "Monitor Dell;211;12;850.00;1250.00#"
    "Monitor AOC;212;7;700.00;1100.00"
)

#função que define o estoque
def definir_estoque(estoque_inicial):
    """Converte a string de estoque inicial em um dicionário.
    
    Args:
        estoque_inicial (str): String contendo os dados iniciais do estoque.
    
    Returns:
        dict: Dicionário representando o estoque.
    """
    estoque = {}
    
    for item in estoque_inicial.split("#"):
        if item:
            descricao, codigo, quantidade, custo, preco = item.split(";")
            estoque[codigo] = {
                "descricao": descricao,
                "codigo": int(codigo),
                "quantidade": int(quantidade),
                "preco": float(preco),
                "custo": float(custo)
            }
    return estoque

#iniciando estoque
estoque = definir_estoque(estoque_inicial)

#Função para adicionar um produto
def adicionar_produto():
    """Adiciona um novo produto ao estoque.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        
    Returns:
        dict: Dicionário atualizado com o novo produto.
    """
    descricao = input("Informe a descrição do produto: ")
    codigo = int(input("Informe o código do produto (deve ser único): "))
    
    # Verifica se o código já existe
    if any(produto['codigo'] == codigo for produto in estoque):
        print("Erro: O código informado já existe. Cadastro não realizado.")
        
        return
    
    quantidade = int(input("Informe a quantidade em estoque: "))
    custo = float(input("Informe o custo do item: "))
    preco = float(input("Informe o preço de venda: "))

    # Adiciona o novo produto ao estoque
    novo_produto = {
        'descricao': descricao,
        'codigo': codigo,
        'quantidade': quantidade,
        'custo': custo,
        'preco': preco
    }
    estoque[codigo] = novo_produto
    print("Produto cadastrado com sucesso!")
    
#Função para remover um produto
def remover_produto(codigo):
    """Remove um produto do estoque pelo código.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        codigo (int): Código do produto a ser removido.
    
    returns:
        dict: Dicionário atualizado sem o produto removido.
    """
    if codigo in estoque:
        del estoque[codigo]
        print("Produto removido com sucesso.")
        return
    print("Erro: Produto não encontrado.")

#Função para listar os produtos
def listar_produtos(estoque):
    """Lista os produtos disponíveis no estoque.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
      
    """
    print("Produtos disponíveis:")
    for codigo, produto in estoque.items():
        print(f"{codigo}: {produto['descricao']} - Quantidade: {produto['quantidade']}")
        
#função que busca um produto pelo codigo ou descricao
def buscar_produto(codigo=None, descricao=None):
    """Busca um produto no estoque pelo código ou descrição.
    
    Args:
        codigo (int): Código do produto a ser buscado.
        descricao (str): Descrição do produto a ser buscado.
        
    Returns:
        list: Lista de produtos que correspondem à busca
    """
    resultado = []
    for produto in estoque:
        if (codigo is not None and produto['codigo'] == codigo) or \
           (descricao is not None and descricao.lower() in produto['descricao'].lower()):
            resultado.append(produto)
    return resultado

#função que ordena o estoque por quantidade
def ordenar_por_quantidade(estoque):
    """Ordena o estoque por quantidade em ordem decrescente.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        
    Returns:
        dict: Dicionário ordenado por quantidade.
    """
    return dict(sorted(estoque.items(), key=lambda x: x[1]['quantidade'], reverse=True))

#função que lista os produtos em falta
def produtos_em_falta(estoque):
    """Lista os produtos que estão em falta no estoque.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        
    Returns:
        list: Lista de produtos em falta
    """
    esgotados = [produto for produto in estoque if produto['quantidade'] == 0]
    if not esgotados:
        print("Não há produtos esgotados.")
        return
    print("\nProdutos Esgotados:")
    for produto in esgotados:
        print(f"{produto['descricao']} - Código: {produto['codigo']}")

#função que filtra os produtos em baixo estoque
def produtos_em_baixo_estoque(estoque, limite=5):
    """Lista os produtos que estão com quantidade abaixo de um limite.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        limite (int): Limite de quantidade para considerar um produto em baixo estoque.
        
    Returns:
        list: Lista de produtos em baixo estoque.
    """
    baixo_estoque = [produto for produto in estoque if produto['quantidade'] < limite]
    if not baixo_estoque:
        print(f"Não há produtos com quantidade abaixo de {limite}.")
        return
    print(f"\nProdutos com quantidade abaixo de {limite}:")
    for produto in baixo_estoque:
        print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']}")
        
#função que atualiza o estoque
def atualizar_estoque(codigo, nova_quantidade):
    """Atualiza a quantidade de um produto no estoque.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        codigo (int): Código do produto a ser atualizado.
        nova_quantidade (int): Nova quantidade do produto.
    
    Returns:
        dict: Dicionário atualizado com a nova quantidade.
            
    """
    for produto in estoque:
        if codigo in estoque:
            if nova_quantidade < 0:
                print("A quantidade não pode ser negativa.")
            return
        estoque[codigo]['quantidade'] = nova_quantidade
    else:
        print("Produto não encontrado.")
    
#função que atualiza o preço de um produto
def atualizar_preco(codigo, novo_preco):
    """Atualiza o preço de um produto no estoque.

    Args:
        estoque (dict): Dicionário representando o estoque.
        codigo (int): Código do produto a ser atualizado.
        novo_preco (float): Novo preço do produto.
        
    Returns:
        dict: Dicionário atualizado com o novo preço.
    """
    for produto in estoque:
        if codigo in estoque:
            if novo_preco < estoque[codigo]['custo']:
                print("O novo preço não pode ser menor que o custo.")
            return
        estoque[codigo]['preco'] = novo_preco
    else:
        print("Produto não encontrado.")

def validar_atualizacao(produto, nova_quantidade=None, novo_preco=None):
    """Valida se a atualização de um produto é válida.

    Args:
        produto (dict): Dicionário representando o produto.
        nova_quantidade (int): Nova quantidade do produto.
        novo_preco (float): Novo preço do produto.

    Returns:
        bool: True se a atualização for válida, False caso contrário.
    """
    if nova_quantidade is not None:
        if nova_quantidade < 0:
            print("Erro: A quantidade não pode ser negativa.")
            return False

    if novo_preco is not None:
        if novo_preco < produto['custo']:
            print("Erro: O novo preço não pode ser menor que o custo.")
            return False

    return True
def calcular_valor_total_estoque():
    """Calcula o valor total do estoque.

    Returns:
        float: Valor total do estoque.
    """
    total = sum(produto['quantidade'] * produto['preco'] for produto in estoque)
    return total

def calcular_lucro_presumido():
    """Calcula o lucro presumido do estoque.

    Returns:
        float: Lucro presumido do estoque.
    """
    lucro_total = sum((produto['preco'] - produto['custo']) * produto['quantidade'] for produto in estoque)
    return lucro_total

def relatorio_geral():
    """Gera um relatório geral do estoque, incluindo custo total e faturamento total.
    
    Args:
        estoque (dict): Dicionário representando o estoque.
        
    returns:
        dict: Dicionário com o relatório geral do estoque.
    """
    print("\nRelatório Geral do Estoque:")
    print("{:<40} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Descrição", "Código", "Quantidade", "Custo", "Preço", "Total"))
    total_custo = 0
    total_faturamento = 0
    
    for produto in estoque:
        total_item = produto['quantidade'] * produto['preco']
        print("{:<40} {:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f}".format(
            produto['descricao'], produto['codigo'], produto['quantidade'],
            produto['custo'], produto['preco'], total_item))
        total_custo += produto['quantidade'] * produto['custo']
        total_faturamento += total_item
    
    print("\nCusto Total do Estoque: {:.2f}".format(total_custo))
    print("Faturamento Total do Estoque: {:.2f}".format(total_faturamento))

# menu de opções
def menu():
    """Exibe o menu de opções disponíveis para o usuário.
    
    Returns:
    menu: Menu de opções disponíveis.
    """
    while True:  # Adicionado loop para manter o menu em execução
        print("\nSistema de Controle de Estoque para Loja de Produtos Eletrônicos")
        print("Selecione uma opção:")
        print("1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("3 - Listar Produtos")
        print("4 - Buscar Produto")
        print("5 - Ordenar por Quantidade")
        print("6 - Produtos em Falta")
        print("7 - Produtos em Baixo Estoque")
        print("8 - Atualizar Estoque")
        print("9 - Atualizar Preço")
        print("10 - Calcular Valor Total do Estoque")
        print("11 - Calcular Lucro Presumido")
        print("12 - Relatório Geral")
        print("0 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            codigo = int(input("Informe o código do produto a ser removido: "))
            remover_produto(codigo)
        elif opcao == '3':
            listar_produtos(estoque)
        elif opcao == '4':
            termo = input("Informe o código ou descrição do produto: ")
            produtos = buscar_produto(codigo=int(termo) if termo.isdigit() else None, descricao=termo)
            if produtos:
                print("\nResultado da Busca:")
                for produto in produtos:
                    print(f"{produto['descricao']} - Código: {produto['codigo']} - Quantidade: {produto['quantidade']}")
            else:
                print("Nenhum produto encontrado.")
        elif opcao == '5':
            estoque_ordenado = ordenar_por_quantidade(estoque)
            print("\nEstoque Ordenado por Quantidade:")
            for codigo, produto in estoque_ordenado.items():
                print(f"{produto['descricao']} - Quantidade: {produto['quantidade']}")
        elif opcao == '6':
            produtos_em_falta(estoque)
        elif opcao == '7':
            limite = int(input("Informe o limite de quantidade para considerar um produto em baixo estoque: "))
            produtos_em_baixo_estoque(estoque, limite)
        elif opcao == '8':
            codigo = int(input("Informe o código do produto a ser atualizado: "))
            nova_quantidade = int(input("Informe a nova quantidade: "))
            atualizar_estoque(codigo, nova_quantidade)
        elif opcao == '9':
            codigo = int(input("Informe o código do produto a ser atualizado: "))
            novo_preco = float(input("Informe o novo preço: "))
            atualizar_preco(codigo, novo_preco)
        elif opcao == '10':
            valor_total = calcular_valor_total_estoque()
            print(f"O valor total do estoque é: R$ {valor_total:.2f}")
        elif opcao == '11':
            lucro = calcular_lucro_presumido()
            print(f"O lucro presumido do estoque é: R$ {lucro:.2f}")
        elif opcao == '12':
            relatorio_geral()
        elif opcao == '0':
            print("Saindo do sistema...")
            break  # Mantido para sair do menu
        else:
            print("Opção inválida. Tente novamente.")

# iniciando o menu
if __name__ == "__main__":
    menu()

        
        