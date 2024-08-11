#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random

dados = int(input("Quantos dados você quer jogar? "))

for i in range(dados):
    print("Dado", i+1, ":", random.randint(1, 6))
    