#Crie uma função chamada imprime_dados que recebe diversos dados de um produto (nome, preço, quantidade em estoque) como argumentos passados obrigatoriamente por palavras-chave e os imprima de forma organizada.

def imprime_dados(nome, preco, quantidade):
    """
    Imprime os dados de um produto de forma organizada.

    Args:
    nome (str): Nome do produto.
    preco (float): Preço do produto.
    quantidade (int): Quantidade em estoque do produto.

    Return: concatenaçãodos dados de forma organizada.
    """
    print("Nome:", nome)
    print("Preço: R$" ,preco)
    print("Quantidade em estoque:", quantidade)

imprime_dados(input("Digite o nome do produto: "), float(input("Digite o preço do produto: ")), int(input("Digite a quantidade em estoque: ")))