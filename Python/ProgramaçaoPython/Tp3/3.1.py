#Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
#CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
#E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
#Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.

def validar_cpf(cpf):
    """Valida e formata um CPF no padrão xxx.xxx.xxx-xx.

    Args:
        cpf (str): O CPF fornecido pelo usuário.

    Returns:
        str: O CPF formatado ou uma mensagem de erro.
    """
    # Remove caracteres não numéricos
    cpf_numeros = ''.join(c for c in cpf if c.isdigit())
    
    # Verifica se o CPF possui exatamente 11 dígitos
    if len(cpf_numeros) != 11:
        return "CPF inválido. O CPF deve conter exatamente 11 dígitos."

    # Formata o CPF
    cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"
    return cpf_formatado

def validar_email(email):
    """Valida e normaliza um e-mail.

    Args:
        email (str): O e-mail fornecido pelo usuário.

    Returns:
        str: O e-mail normalizado ou uma mensagem de erro.
    """
    # Verifica a presença do '@' e um '.' após '@'
    if '@' not in email or '.' not in email.split('@')[-1]:
        return "E-mail inválido. Verifique o formato do e-mail."

    # Normaliza o e-mail para minúsculas
    email_normalizado = email.lower()
    return email_normalizado

def validar_telefone(telefone):
    """Valida e formata um número de telefone.

    Args:
        telefone (str): O telefone fornecido pelo usuário.

    Returns:
        tuple: O número de telefone formatado e o número inteiro.
    """
    # Remove caracteres não numéricos
    telefone_numeros = ''.join(c for c in telefone if c.isdigit())
    
    # Verifica se o telefone possui exatamente 10 ou 11 dígitos
    if len(telefone_numeros) not in [10, 11]:
        return "Telefone inválido. O número deve conter 10 ou 11 dígitos.", None

    # Formata o telefone
    if len(telefone_numeros) == 11:
        telefone_formatado = f"({telefone_numeros[:2]}) {telefone_numeros[2:7]}-{telefone_numeros[7:]}"
    else:
        telefone_formatado = f"({telefone_numeros[:2]}) {telefone_numeros[2:6]}-{telefone_numeros[6:]}"
    
    return telefone_formatado, int(telefone_numeros)

def main():
    """Função principal para solicitar e validar os dados do usuário."""
    # Solicita dados do usuário
    cpf = input("Digite seu CPF (xxx.xxx.xxx-xx): ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone (inclua DDD): ")

    # Valida e exibe resultados
    cpf_formatado = validar_cpf(cpf)
    email_normalizado = validar_email(email)
    telefone_formatado, telefone_inteiro = validar_telefone(telefone)
    
    print("\nResultados da validação:")
    print(f"CPF: {cpf_formatado}")
    print(f"E-mail: {email_normalizado}")
    if telefone_inteiro is not None:
        print(f"Telefone: {telefone_formatado}")
        print(f"Número inteiro: {telefone_inteiro}")
    else:
        print(f"Telefone: {telefone_formatado}")

# Executa o programa
if __name__ == "__main__":
    main()

