#calcular o resultado de uma expressão matemática básica fornecida como string pelo usuário, ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.
#Exemplo: '2 + 3 * 4' Resultado: 14.

#iniciando variaveis
expressao = ""
resultado = 0

#input e validação
while not expressao.replace(" ", "").replace("+", "").replace("-", "").replace("*", "").replace("/", "").isdigit() or expressao == "":
    expressao = input("Digite uma expressão matemática básica: ")
    
#definição da função
def calculo_basico(expressao):
    """função que calcula o resultado de uma expressão matemática básica fornecida como string pelo usuário
    
    Args:
        expressao (str): A expressão matemática básica fornecida pelo usuário.
    Returns:
        str: O resultado da expressão matemática básica fornecida pelo usuário.
    """
    resultado = eval(expressao) # Avalia a expressão.
    print("O resultado da expressão é: ", resultado) # Exibe o resultado.
    
    return resultado




#output
calculo_basico(expressao)
