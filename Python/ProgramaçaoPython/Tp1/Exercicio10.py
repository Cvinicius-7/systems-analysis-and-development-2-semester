#Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random

personagens = ["João", "Maria", "Pedro", "Ana"]
acoes = ["correu", "saltou", "dançou", "cantou"]
locais = ["na floresta", "na praia", "na montanha", "no deserto"]

personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

print(personagem, acao, local)
