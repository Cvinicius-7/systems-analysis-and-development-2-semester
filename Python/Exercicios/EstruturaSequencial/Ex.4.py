#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da internet em Mbps: "))

tempo_download = tamanho_arquivo / velocidade_internet
tempo_download = tempo_download / 60

print("O tempo estimado para download é de", round(tempo_download,2), "minutos")

