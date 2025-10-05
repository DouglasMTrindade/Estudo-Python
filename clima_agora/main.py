import os
import localizacao
from dotenv import load_dotenv
import requests

dados_local = localizacao.busca_localizacao()

print(dados_local['city'])