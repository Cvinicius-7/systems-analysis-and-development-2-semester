#Escreva um programa que receba uma lista de números (você pode definir a lista inicialmente, mas certifique-se que o código funcionará para quaisquer listas numéricas) e utilize um loop for para calcular a média dos valores da lista.

lista = input("Digite uma lista de números separados por espaço: ").split()
lista = [int(i) for i in lista]

for i in range(len(lista)):
    soma = 0
    soma += lista[i]
    media = soma / len(lista)
    
print("A média dos valores da lista é: ", int(media))
