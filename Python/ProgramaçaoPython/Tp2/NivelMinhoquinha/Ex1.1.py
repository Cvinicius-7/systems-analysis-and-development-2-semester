#Crie um programa que receba uma string como entrada do usuário e use um loop for para criar uma lista com cada caractere da string.

string_usuario = input("Digite uma string: ")
lista = []

for i in string_usuario:
    lista.append(i)
    
print(lista)