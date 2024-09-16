#Crie um programa que solicite um nome completo ao usuário e formate-o de forma que todas as palavras comecem com letra maiúscula e o restante seja minúsculo e exiba-o na tela.

#input e validação, usuario não deve digitar numeros nem input vazio
nome_completo = input("Digite seu nome completo: ")

while nome_completo.isdigit() or nome_completo == "":
    nome_completo = input("Digite seu nome completo: ")
    
    #formatação
nome_completo = nome_completo.title()

#output
print(nome_completo)
