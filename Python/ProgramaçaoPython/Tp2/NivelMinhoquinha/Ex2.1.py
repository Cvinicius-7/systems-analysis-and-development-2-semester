#Crie um programa que peça ao usuário para inserir números um de cada vez até que ele digite 0. Armazene esses números em uma lista usando um loop while.

numero_usuario = 1
lista = []

while numero_usuario != 0:
    numero_usuario = int(input("Digite um número(0 Encerra o Programa): "))
    lista.append(numero_usuario)
    
print("Sua lista é : " , lista)