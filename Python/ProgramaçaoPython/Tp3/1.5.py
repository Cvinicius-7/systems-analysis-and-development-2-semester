#Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos

#iniciando variaveis
numero = ""
soma = 0

#input e validação
while not numero.isdigit() or numero == "":
    numero = input("Digite um número: ")
    
#calculo da soma
for i in numero:
    soma += int(i)
    
#output
print("A soma dos digitos do número é: ", soma)
