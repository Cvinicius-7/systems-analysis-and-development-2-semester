import re
from collections import Counter

def extrair_clausulas_com_valores(texto):
    """Extrai cláusulas que mencionam valores monetários.

    Args:
        texto (str): O texto completo do contrato.

    Returns:
        list: Lista de cláusulas que mencionam valores monetários.
    """
    # Expressão regular para encontrar valores monetários no formato "R$ x.xxx,xx" ou "x.xxx,xx"
    padrao_valor = r'\b(?:R\$ ?\d{1,3}(?:\.\d{3})*,\d{2}|\d{1,3}(?:\.\d{3})*,\d{2})\b'
    clausulas_com_valores = []

    # Quebrar o texto em cláusulas (supondo que cada cláusula está separada por um ponto final)
    clausulas = texto.split('. ')
    
    for clausula in clausulas:
        if re.search(padrao_valor, clausula):
            clausulas_com_valores.append(clausula)
    
    return clausulas_com_valores

def contar_termos_legais(texto, termos_legais):
    """Conta a frequência de cada termo legal no texto.

    Args:
        texto (str): O texto completo do contrato.
        termos_legais (list): Lista de termos legais a serem contados.

    Returns:
        dict: Dicionário com termos legais e suas frequências, ordenado por frequência decrescente.
    """
    # Converter o texto para minúsculas e criar um contador
    texto = texto.lower()
    contador = Counter()
    
    for termo in termos_legais:
        # Contar a ocorrência do termo legal no texto
        termo_lower = termo.lower()
        contador[termo_lower] = texto.count(termo_lower)
    
    # Ordenar por frequência decrescente
    frequencias = dict(sorted(contador.items(), key=lambda item: item[1], reverse=True))
    
    return frequencias

def main():
    """Função principal para processar o contrato e contar termos legais."""
    
    # Recebe o texto do contrato do usuário
    texto = input("Digite o texto completo do contrato:\n")
    
    # Extrai cláusulas que mencionam valores monetários
    clausulas_com_valores = extrair_clausulas_com_valores(texto)
    print("\nCláusulas que mencionam valores monetários:")
    for clausula in clausulas_com_valores:
        print(f"- {clausula}")
    
    # Recebe a lista de termos legais para contar
    termos_legais_input = input("\nDigite a lista de termos legais separados por vírgula:\n")
    termos_legais = [termo.strip() for termo in termos_legais_input.split(',')]
    
    # Conta a frequência dos termos legais
    frequencias = contar_termos_legais(texto, termos_legais)
    print("\nFrequência dos termos legais:")
    for termo, frequencia in frequencias.items():
        print(f"{termo}: {frequencia} ocorrência(s)")

# Executa o programa
if __name__ == "__main__":
    main()
