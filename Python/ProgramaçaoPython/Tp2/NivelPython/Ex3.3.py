#Escreva um programa que utilize um laço while para solicitar ao usuário que informe a hora do registro da temperatura (em um número inteiro) seguido do valor da temperatura registrada. Seu programa deverá conter função de validação da entrada do usuário para garantir que a hora descrita esteja entre 0h e 23h e que a temperatura informada esteja entre -15ºC e 60ºC. E em seguida armazene as informações em duas listas, uma com os horários e outra com as temperaturas.

def validar_hora(hora):
    return 0 <= hora <= 23

def validar_temperatura(temperatura):
    return -15 <= temperatura <= 60

def calcular_media_ponderada(horarios, temperaturas):
    
    total_ponderado = 0
    total_intervalo = 0
    
    for i in range(1, len(horarios)):
        intervalo = horarios[i] - horarios[i-1]
        
        temperatura_media = (temperaturas[i] + temperaturas[i-1]) / 2
        total_ponderado += temperatura_media * intervalo
        total_intervalo += intervalo
    
    media_ponderada = total_ponderado / total_intervalo
    return media_ponderada, min(temperaturas), max(temperaturas)

def encontrar_extremos(horarios, temperaturas):
    temp_min = min(temperaturas)
    temp_max = max(temperaturas)
    hora_min = horarios[temperaturas.index(temp_min)]
    hora_max = horarios[temperaturas.index(temp_max)]
    
    return hora_min, temp_min, hora_max, temp_max


horarios = []
temperaturas = []
    
while True:
    entrada = input("Digite a hora do registro (0 a 23), o valor da temperatura registrada (-15 a 60) ou 'Fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        dados = entrada.split()
        hora = int(dados[0])
        temperatura = float(dados[1])
        
        if not validar_hora(hora) or not validar_temperatura(temperatura):
             print("Dados inválidos. Hora deve estar entre 0 e 23 e temperatura entre -15ºC e 60ºC.")
             continue
         
        horarios.append(hora)
        temperaturas.append(temperatura)
    except (ValueError, IndexError):
        print("Entrada inválida. Formato esperado: hora temperatura.")
    
if horarios:
        media_ponderada, temp_min, temp_max = calcular_media_ponderada(horarios, temperaturas)
        hora_min, _, hora_max, _ = encontrar_extremos(horarios, temperaturas)
        
        print(f"\nMédia ponderada das temperaturas: {media_ponderada:.2f}°C")
        if 20 <= media_ponderada <= 30:
            print("A média ponderada está dentro do intervalo de segurança (20°C a 30°C).")
        else:
            print("A média ponderada está fora do intervalo de segurança (20°C a 30°C).")
        
        if temp_min is not None and temp_max is not None:
            print(f"Temperatura mais baixa: {temp_min:.2f}°C às {horarios[temperaturas.index(temp_min)]}h")
            print(f"Temperatura mais alta: {temp_max:.2f}°C às {horarios[temperaturas.index(temp_max)]}h")

