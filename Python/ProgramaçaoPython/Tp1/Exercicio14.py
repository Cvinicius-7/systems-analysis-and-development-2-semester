#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

opcao1 = 0
opcao2 = 0
opcao3 = 0

opcao = input("Digite a opção desejada (1, 2 ou 3) ou 0 para sair: ")

while opcao != "0":
    if opcao == "1":
        opcao1 += 1
    elif opcao == "2":
        opcao2 += 1
    elif opcao == "3":
        opcao3 += 1
    else:
        print("Opção inválida.")
    opcao = input("Digite a opção desejada (1, 2 ou 3) ou 0 para sair: ")
    
print("Opção 1:", opcao1, "votos")
print("Opção 2:", opcao2, "votos")
print("Opção 3:", opcao3, "votos")
