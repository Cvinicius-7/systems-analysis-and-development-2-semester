#Defina uma função chamada potencia que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. A função deve calcular e retornar a base elevada ao expoente.

def potencia(base, expoente = 2):
    """Calcula a potência de um número.

    Args:
        base (int | float): O número base.
        expoente (int): o expoente no qual sera elevado. o número padão é 2.
    Returns:
        int | float: O resultado da potência.
    """
    print(base ** expoente) 

potencia(int(input("Digite a base: ")), int(input("Digite o expoente: ")))

