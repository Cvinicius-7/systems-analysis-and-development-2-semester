#Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.


#input texto fornecido	
texto_fornecido = "O rato roeu a roupa do rei de roma"


#validação para que o usuario não digite input vazio e nem uma palavra que não existe no texto fornecido
while palavra_substituida == "" or palavra_substituida not in texto_fornecido:
    palavra_substituida = input("Digite a palavra a ser substituida: ")
    palavra_substituta = input("Digite a nova palavra: ")
    

#substituição
texto_fornecido = texto_fornecido.replace(palavra_substituida, palavra_substituta)

#output
print("O texto novo será :  ", texto_fornecido)

