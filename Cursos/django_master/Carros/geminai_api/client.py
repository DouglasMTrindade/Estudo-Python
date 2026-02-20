import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_car_ai_bio(model, brand, year):
    # Carrega variáveis do .env
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Chave da API Gemini não encontrada. Configure o arquivo .env."

    genai.configure(api_key=api_key)
    prompt = (
        "Escreva uma breve descrição para um carro com as seguintes características: "
        f"modelo {model}, marca {brand} e ano de fabricação {year} em no máximo 250 caracteres."
    )
    try:
        model_gemini = genai.GenerativeModel("gemini-3-flash-preview")
        response = model_gemini.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao acessar Gemini: {e}"