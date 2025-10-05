import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('IPINFO_API_KEY')

def busca_localizacao ():
    """
    Busca a localização atual baseada no IP usando a API do ipinfo.io.
    
    Retorna:
        dict: Dados da localização (cidade, região, país, lat/long, etc.) ou None em caso de erro
    """
    
    if not api_key:
        print("Erro, Chave não encontrada no .env")
        return None
    url = f'https://ipinfo.io/json?token={api_key}'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None