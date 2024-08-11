#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

palavras = input("Digite algumas palavras separadas por espaços: ").split()

for palavra in palavras:
    if len(palavra) < 5:
        print(palavra, "é uma palavra curta.")
    else:
        print(palavra, "é uma palavra longa.")