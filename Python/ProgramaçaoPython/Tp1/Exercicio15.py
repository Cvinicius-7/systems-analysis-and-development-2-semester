#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

print("Você está em um taxi e o motorista pergunta para onde você quer ir. (1) Shopping (2) Aeroporto")

if input() == "1":
    print("Você chega no shopping e encontra um amigo. (1) Ir ao cinema (2) Ir ao restaurante")
    if input() == "1":
        print("Você assiste um filme e se diverte.")
    else:
        print("Você vai ao restaurante e come uma refeição saborosa.")
else:
    print("Você chega no aeroporto e descobre que seu voo foi cancelado. (1) Esperar por outro voo (2) Voltar para casa")
    if input() == "1":
        print("Você espera por horas até conseguir embarcar em outro voo.")
    else:
        print("Você volta para casa e decide viajar em outra data.")
        