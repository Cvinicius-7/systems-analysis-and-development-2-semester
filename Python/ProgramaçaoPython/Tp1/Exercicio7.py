#Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 24.9:
    print("Peso normal.")
elif imc < 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")