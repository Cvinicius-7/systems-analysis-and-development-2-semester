#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato

ganho_hora = float(input("Digite quanto você ganha por hora: "))
horas_mensais = int(input("Digite quantas horas você trabalha por mês: "))

salario_bruto = ganho_hora * horas_mensais
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("+ Salário Bruto: R$", salario_bruto)
print("- Imposto de Renda: R$", imposto_renda)
print(" - INSS: R$", inss)
print(" - Sindicato: R$", sindicato)
print(" + Salário Líquido: R$", round(salario_liquido,2))