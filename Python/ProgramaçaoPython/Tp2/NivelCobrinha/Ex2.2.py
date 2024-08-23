#Crie uma função chamada maior_valor que receba três números como trê argumentos posicionais, exiba o maior número na tela e retorne uma lista ordenada contendo estes números

def maior_valor(num1, num2, num3):
    """Recebe três números e retorna o maior deles.

    Args:
        num1 (int | float): O primeiro número.
        num2 (int | float): O segundo número.
        num3 (int | float): O terceiro número.
    Returns:
        list: Uma lista ordenada contendo os três números.
    """
    lista = [num1, num2, num3]
    print(max(lista))
    return sorted(lista)

print(maior_valor(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))))