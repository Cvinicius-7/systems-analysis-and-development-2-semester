#Crie um programa que simule o crescimento de um investimento ao longo de um período. O programa deve solicitar ao usuário o valor inicial do investimento, a taxa de juros anual e o número de anos. Em seguida, escreva uma função que calcule o valor final do investimento ao final de cada ano e armazene esses valores em uma lista. Imprima o valor acumulado ano a ano (lembre-se que se trata de juros compostos).

valor_investimento = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros anual: "))
anos = int(input("Digite o número de anos: "))

def valor_final_investimento(valor_investimento, taxa_juros, anos):
    lista = []
    
    for i in range(1, anos + 1):
        
        valor_investimento = valor_investimento * (1 + taxa_juros)
        lista.append(round(valor_investimento, 2))
        
    return lista

print(valor_final_investimento(valor_investimento, taxa_juros, anos),2)