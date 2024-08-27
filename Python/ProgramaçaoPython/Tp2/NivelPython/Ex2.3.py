#Escreva um programa que ajude um motorista a calcular o consumo de combustível de seu veículo. O programa deve solicitar ao usuário que insira a distância percorrida e a quantidade de combustível consumido em várias viagens. Essas informações devem ser armazenadas em uma lista. Em seguida, crie uma função que percorra essa lista e calcule o consumo médio de combustível (km/l) para cada viagem e para o total de todas as viagens. 
def obter_viagem():
    viagens = []
    while True:
        distancia = float(input("Digite a distância percorrida em km (ou 0 para parar): "))
        if distancia == 0:
            break
        combustivel = float(input("Digite a quantidade de combustível consumido em Litros: "))
        viagens.append([distancia, combustivel])
    return viagens

def consumo_medio(viagens):
    distancia_total = 0
    combustivel_total = 0
    
    for viagem in viagens:
        distancia, combustivel = viagem
        consumo = distancia / combustivel
        
        print("O consumo médio da viagem foi de: ", round(consumo, 2), "km/l")
        
        distancia_total += distancia
        combustivel_total += combustivel
        
    consumo_total = distancia_total / combustivel_total
    print("O consumo médio total foi de: ", round(consumo_total, 2),"km/l")

viagens = obter_viagem()
consumo_medio(viagens)

    
