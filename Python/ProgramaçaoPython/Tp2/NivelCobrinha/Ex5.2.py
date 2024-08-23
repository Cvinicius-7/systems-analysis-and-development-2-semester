#Defina uma função chamada exibir_mensagem que receba um argumento obrigatório mensagem e um argumento opcional repeticoes, onde repeticoes tem um valor padrão de 1. A função deve imprimir a mensagem o número de vezes especificado por repeticoes. 

def exibir_mensagem(mensagem, repeticoes = 1):
    """Exibe uma mensagem na tela.

    Args:
        mensagem (str): A mensagem a ser exibida.
        repeticoes (int): O número de vezes que a mensagem será exibida. O padrão é 1.
        
    Return: A mensagem exibida na tela repetidas vezes.
    """
    for i in range(repeticoes):
        print(mensagem)
    
exibir_mensagem(input("Digite a mensagem: "), int(input("Digite o número de repetições: ")))   