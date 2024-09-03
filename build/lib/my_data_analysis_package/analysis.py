# my_data_analysis_package/analysis.py

import pandas as pd

def analyze_data(data):
    """
    Função simples para análise de dados.
    
    Args:
        data (pd.DataFrame): Um DataFrame pandas para análise.
    
    Returns:
        pd.DataFrame: Retorna um DataFrame com estatísticas descritivas.
    """
    return data.describe()
