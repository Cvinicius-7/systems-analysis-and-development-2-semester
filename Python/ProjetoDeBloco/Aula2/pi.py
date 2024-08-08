pi = 3.141592653589793
print('Valor de pi: ',pi)
print()
raio = input('Digite o raio ')
altura = input('Digite a altura ')
raio = float(raio)
altura = float(altura)
volume = round((pi * raio ** 2 * altura) / 3 ,2)
print(f"O volume é: {volume}")
