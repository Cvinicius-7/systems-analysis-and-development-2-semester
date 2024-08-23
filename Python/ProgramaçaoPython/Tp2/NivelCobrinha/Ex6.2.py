#Defina uma função chamada gerar_lista_pares que receba um número n, fornecido pelo usuário, como argumento e retorne uma lista contendo todos os números pares de 0 até n. Utilize um laço for para preencher a lista.

def gerar_lista_pares(n):
    """Gera uma lista de números pares até n.

    Args:
        n (int): O número limite da lista.
    Returns:
        list: Uma lista contendo os números pares até n.
    """
    lista = []
    for i in range(n + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista

print(gerar_lista_pares(int(input("Digite um número: "))))