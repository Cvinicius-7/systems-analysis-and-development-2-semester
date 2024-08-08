#Declaração de variáveis string
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#Concatenação de strings
nome_completo = nome + ' ' + sobrenome
print('Seu nome completo é: ' + nome_completo)

#Acesso a um caractere específico
primeira_letra = nome_completo[0]
print('A primeira letra do seu nome é: ' + primeira_letra)