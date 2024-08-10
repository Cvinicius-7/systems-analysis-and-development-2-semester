#Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números.

primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")
operacao = input("Escolha sua operação: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

match operacao:
    case "1":
        resultado = round(float(primeiro_numero) + float(segundo_numero),2)
        print("Soma:", resultado)
    case "2":
        resultado = float(primeiro_numero) - float(segundo_numero)
        print("Subtração:", resultado)
    case "3":
        resultado = float(primeiro_numero) * float(segundo_numero)
        print("Multiplicação:", resultado)
    case "4":
        resultado = round(float(primeiro_numero) / float(segundo_numero),2)
        print("Divisão:", resultado)
    case _:
        print("Digite uma operação válida.")
   