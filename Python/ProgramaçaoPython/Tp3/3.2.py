#Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário". O programa deve calcular e exibir o valor total das vendas para cada produto.
#Crie uma função que receba a lista de transações e retorne o produto mais vendido (baseado na quantidade) e o produto que gerou a maior receita total.
#Escreva um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário. Exiba os valores convertidos no formato monetário adequado.

def calcular_vendas_por_produto(transacoes):
    """
    Calcula o valor total de vendas para cada produto e a quantidade total vendida.

    Args:
        transacoes (list): Lista de transações no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário".

    Returns:
        dict: Dicionário com o nome do produto como chave e um tuplo (quantidade_total, valor_total) como valor.
    """
    vendas = {}

    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(',')
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario

        if nome_produto in vendas:
            vendas[nome_produto][0] += quantidade
            vendas[nome_produto][1] += valor_total
        else:
            vendas[nome_produto] = [quantidade, valor_total]

    return vendas

def produto_mais_vendido_e_mais_rentavel(vendas):
    """
    Determina o produto mais vendido e o produto que gerou a maior receita total.

    Args:
        vendas (dict): Dicionário com o nome do produto como chave e um tuplo (quantidade_total, valor_total) como valor.

    Returns:
        tuple: (produto_mais_vendido, produto_mais_rentavel)
    """
    produto_mais_vendido = max(vendas.items(), key=lambda x: x[1][0])
    produto_mais_rentavel = max(vendas.items(), key=lambda x: x[1][1])
    
    return produto_mais_vendido, produto_mais_rentavel

def formatar_moeda(valor):
    """Formata um valor como moeda no padrão brasileiro (R$ x.xxx,xx)."""
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def main():
    """Função principal para processar transações e converter valores para nova moeda."""
    
    # Recebe a lista de transações do usuário
    transacoes = []
    print("Digite as transações (ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário). Digite 'fim' para terminar.")
    
    while True:
        transacao = input("Digite a transação: ")
        if transacao.lower() == 'fim':
            break
        transacoes.append(transacao)
    
    # Calcula o valor total de vendas para cada produto e a quantidade total vendida
    vendas = calcular_vendas_por_produto(transacoes)
    
    # Determina o produto mais vendido e o produto que gerou a maior receita
    produto_mais_vendido, produto_mais_rentavel = produto_mais_vendido_e_mais_rentavel(vendas)
    
    # Exibe os resultados
    print("\nResumo das vendas:")
    for produto, (quantidade, valor_total) in vendas.items():
        print(f"Produto: {produto}, Quantidade Total: {quantidade}, Valor Total: {formatar_moeda(valor_total)}")
    
    print(f"\nProduto mais vendido: {produto_mais_vendido[0]} com {produto_mais_vendido[1][0]} unidades vendidas.")
    print(f"Produto mais rentável: {produto_mais_rentavel[0]} com receita total de {formatar_moeda(produto_mais_rentavel[1][1])}.")
    
    # Solicita o fator de conversão para nova moeda
    try:
        fator_conversao = float(input("\nDigite o fator de conversão para a nova moeda: "))
    except ValueError:
        print("Fator de conversão inválido. Por favor, insira um número.")
        return

    # Converte e exibe os valores em nova moeda
    print("\nValores convertidos para a nova moeda:")
    for produto, (quantidade, valor_total) in vendas.items():
        valor_convertido = valor_total * fator_conversao
        print(f"Produto: {produto}, Valor Total Convertido: {formatar_moeda(valor_convertido)}")

# Executa o programa
if __name__ == "__main__":
    main()
