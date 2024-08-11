#Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

minutos = int(input("Digite um número de minutos: "))

minutos_restantes = minutos % 60
horas = minutos // 60

print(minutos, "minutos são", horas, "horas e", minutos_restantes, "minutos.")

horas = int(input("Digite um número de horas: "))
minutos = int(input("Digite um número de minutos: "))

minutos_totais = horas * 60 + minutos

print(horas, "horas e", minutos, "minutos são", minutos_totais, "minutos.")

