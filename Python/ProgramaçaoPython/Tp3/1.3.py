#Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.]

#recebendo input do usuario, e validação para que o usuario não digite input vazio e nem input com numeros
texto = ""

while texto.isdigit() or texto == "":
    texto = input("Digite um texto: ")

#função que retorna a palavra mais longa do texto  
def palavra_mais_longa(texto):
    """Retorna a palavra mais longa em um texto, desconsiderando a pontuação.

    Args:
       texto (str): O texto do qual encontrar a palavra mais longa.
    Returns:
       str: A palavra mais longa do texto.
    """
    
    texto = texto.replace(",", "").replace(".", "") # Remove a pontuação.
    texto = texto.split() # Separa o texto em palavras.
    
    texto = sorted(texto, key=len, reverse=True)# Ordena as palavras por tamanho.
    
    return texto[0] # Retorna a primeira palavra, que é a mais longa.

print("A palavra mais longa do seu texto é: ",palavra_mais_longa(texto))


