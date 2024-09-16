#Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

#input e validação
frase = ""

while frase.isdigit() or frase == "":
    frase = input("Digite uma frase: ")
 
#definindo a função  
def contar_caracteres(frase):
    """função que conta os caracteres, palavras e espaços em branco
    
    Args:
        texto (str): A frase do qual contar os caracteres, palavras e espaços em branco.
    Returns:
        str: A quantidade de caracteres, palavras e espaços em branco.
    """
    caracteres = len(frase)
    palavras = len(frase.split())
    espacos = frase.count(" ")
    print("A frase tem ", caracteres, "caracteres, ", palavras, "palavras e ", espacos, "espaços em branco")

#output    
contar_caracteres(frase)