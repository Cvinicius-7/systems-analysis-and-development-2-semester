#Usando a mesma implementação da questão 5 modifique a função para que, caso nenhum argumento seja passado, exiba uma saudação genérica, como "Olá, amigo!".

def saudacao(nome="amigo"):
    print("Olá,", nome + "!")

saudacao(input("Digite seu nome (pressione Enter para uma saudação genérica): ") or "amigo")
