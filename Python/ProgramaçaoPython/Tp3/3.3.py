import random
import string

# Função para gerar senhas aleatórias seguras
def gerar_senha(tamanho=12):
    """Gera uma senha aleatória segura com letras maiúsculas, minúsculas, números e caracteres especiais.

    Args:
        tamanho (int): O comprimento da senha gerada.

    Returns:
        str: A senha gerada.
    """
    if tamanho < 8:
        raise ValueError("A senha deve ter no mínimo 8 caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Função para verificar a segurança da senha
def verificar_senha(senha):
    """Verifica se a senha atende aos critérios de segurança.

    Args:
        senha (str): A senha a ser verificada.

    Returns:
        bool: True se a senha atender aos critérios de segurança, False caso contrário.
    """
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.islower() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in string.punctuation for c in senha):
        return False
    return True

# Função para sugerir uma nova senha
def sugerir_nova_senha():
    """Sugere uma nova senha segura."""
    return gerar_senha()

# Função para criptografar a senha usando uma cifra de substituição
def criptografar_senha(senha, deslocamento):
    """Criptografa a senha usando uma cifra de substituição com deslocamento.

    Args:
        senha (str): A senha a ser criptografada.
        deslocamento (int): O número de posições para deslocar cada caractere.

    Returns:
        str: A senha criptografada.
    """
    caracteres_ascii = string.printable
    tabela_criptografia = caracteres_ascii[deslocamento:] + caracteres_ascii[:deslocamento]
    tabela_traducao = str.maketrans(caracteres_ascii, tabela_criptografia)
    return senha.translate(tabela_traducao)

# Função para descriptografar a senha
def descriptografar_senha(senha_criptografada, deslocamento):
    """Descriptografa a senha usando uma cifra de substituição com deslocamento.

    Args:
        senha_criptografada (str): A senha criptografada.
        deslocamento (int): O número de posições para deslocar cada caractere.

    Returns:
        str: A senha descriptografada.
    """
    caracteres_ascii = string.printable
    tabela_criptografia = caracteres_ascii[-deslocamento:] + caracteres_ascii[:-deslocamento]
    tabela_traducao = str.maketrans(tabela_criptografia, caracteres_ascii)
    return senha_criptografada.translate(tabela_traducao)

def main():
    """Função principal para testar a funcionalidade de gerenciamento de senhas."""
    while True:
        print("1. Gerar senha aleatória")
        print("2. Verificar senha")
        print("3. Criptografar senha")
        print("4. Descriptografar senha")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tamanho = int(input("Digite o comprimento da senha (mínimo 8): "))
            try:
                senha = gerar_senha(tamanho)
                print(f"Senha gerada: {senha}")
            except ValueError as e:
                print(e)

        elif escolha == '2':
            senha = input("Digite a senha para verificação: ")
            if verificar_senha(senha):
                print("A senha atende aos critérios de segurança.")
            else:
                print("A senha não atende aos critérios de segurança.")
                nova_senha = sugerir_nova_senha()
                print(f"Sugestão de nova senha: {nova_senha}")

        elif escolha == '3':
            senha = input("Digite a senha para criptografar: ")
            deslocamento = int(input("Digite o deslocamento para a cifra de substituição: "))
            senha_criptografada = criptografar_senha(senha, deslocamento)
            print(f"Senha criptografada: {senha_criptografada}")

        elif escolha == '4':
            senha_criptografada = input("Digite a senha criptografada para descriptografar: ")
            deslocamento = int(input("Digite o deslocamento usado para criptografia: "))
            senha_descriptografada = descriptografar_senha(senha_criptografada, deslocamento)
            print(f"Senha descriptografada: {senha_descriptografada}")

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
