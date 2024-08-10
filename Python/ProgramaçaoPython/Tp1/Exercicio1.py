#1 Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")
soma = round(float(primeiro_numero) + float(segundo_numero),2)
subtracao = float(primeiro_numero) - float(segundo_numero)
multiplicacao = float(primeiro_numero) * float(segundo_numero)
divisao = round(float(primeiro_numero) / float(segundo_numero),2)
divisao_inteira = float(primeiro_numero) // float(segundo_numero)

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão inteira:", divisao_inteira)





















