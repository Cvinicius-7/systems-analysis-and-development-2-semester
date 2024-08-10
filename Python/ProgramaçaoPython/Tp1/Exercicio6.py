#Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

num_secreto = 42

palpite = int(input("Digite seu palpite: "))

while palpite != num_secreto:
    if palpite > num_secreto:
        print("Muito alto.")
    else:
        print("Muito baixo.")
    palpite = int(input("Digite seu palpite: "))
    
print("Parabéns! Você acertou o número secreto.")
