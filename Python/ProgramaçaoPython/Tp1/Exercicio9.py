#Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.

desconto = 0
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 500:
    desconto = 0.25 * valor_compra
elif valor_compra > 200:
    desconto = 0.15 * valor_compra
elif valor_compra > 100:
    desconto = 0.10 * valor_compra
    
    print("Desconto de R$", desconto)
    print("Valor final: R$", valor_compra - desconto)