#Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro de dois mil e vinte e quatro".
def data_por_extenso(data):
    """Converte uma data no formato "dd/mm/aaaa" para uma string textual.

    Args:
        data (str): A data no formato "dd/mm/aaaa".

    Returns:
        str: A data no formato textual.
    """
    # Listas de nomes por extenso
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    unidades = [
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
        'sete', 'oito', 'nove'
    ]
    dezenas = [
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
        'dezessete', 'dezoito', 'dezenove'
    ]
    dezenas_10_90 = [
        '', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 
        'setenta', 'oitenta', 'noventa'
    ]
    centenas = [
        'cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
    ]
    milhares = [
        '', 'mil', 'dois mil', 'três mil', 'quatro mil', 'cinco mil',
        'seis mil', 'sete mil', 'oito mil', 'nove mil'
    ]
    
    def numero_por_extenso(num):
        """Converte um número em formato de texto.

        Args:
            num (int): O número a ser convertido.

        Returns:
            str: O número em formato
        """
        
        if 0 <= num <= 9:
            return unidades[num]
        elif 10 <= num <= 19:
            return dezenas[num - 10]
        elif 20 <= num <= 99:
            dezena, unidade = divmod(num, 10)
            return dezenas_10_90[dezena] + ('' if unidade == 0 else ' e ' + unidades[unidade])
        elif 100 <= num <= 999:
            centena, resto = divmod(num, 100)
            return (centenas[centena] + ('' if resto == 0 else ' e ' + numero_por_extenso(resto)))
        elif 1000 <= num <= 9999:
            milhar, resto = divmod(num, 1000)
            return (milhares[milhar] + ('' if resto == 0 else ' e ' + numero_por_extenso(resto)))
        return str(num)
    
    # Separar a data em dia, mês e ano
    dia, mes, ano = map(int, data.split('/'))
    
    # Obter as partes da data por extenso
    dia_extenso = numero_por_extenso(dia)
    mes_extenso = meses[mes - 1]
    
    # Converter ano para texto
    ano_extenso = numero_por_extenso(ano)

    # Formatar a data completa
    return f"{dia_extenso} de {mes_extenso} de {ano_extenso}"


#input e validação
data = ""
while data == "" or len(data) != 10:
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    
    
#output
print("Sua data por extenso é: "data_por_extenso(data))
