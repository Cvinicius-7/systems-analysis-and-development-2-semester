#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

palavra = input("Digite uma palavra ou frase: ").lower()

if palavra == palavra[::-1]:
    print("Esta palavra ou frase é um palíndromo.")
else:
    print("Esta palavra ou frase não é um palíndromo.")
