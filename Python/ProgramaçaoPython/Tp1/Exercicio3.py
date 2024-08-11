#Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

primeiro_nome = input("Digite o primeiro nome: ")
segundo_nome = input("Digite o segundo nome: ")

print("Nome criativo:", primeiro_nome[:3] + segundo_nome[-3:])