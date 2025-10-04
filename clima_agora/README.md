# 🌦️ Projeto: Consulta de Clima com Localização Automática

Este projeto em **Python** consulta informações climáticas atuais usando a **API do OpenWeatherMap** 🌤️.  
O sistema identifica automaticamente a **localização do usuário** através de uma API de geolocalização baseada em IP e exibe na tela dados como:

- 🌍 Localização detectada  
- 🌡️ Temperatura atual  
- 🤔 Sensação térmica  
- 💨 Velocidade do vento  
- ☁️ Condição do tempo  

Além disso, o programa registra todas as consultas realizadas em um arquivo `consultas.txt`.

---

## 🧠 Objetivo

Este é um projeto de **aprendizado**, desenvolvido para praticar:
- Consumo de **APIs REST** com Python (`requests`, `json`)
- Manipulação de dados retornados em formato **JSON**
- Estruturação modular de código
- Escrita e leitura de **arquivos de log**
- Boas práticas de programação e documentação

---

## ⚙️ Tecnologias utilizadas

- **Python 3.x**
- **Bibliotecas:**
  - `requests` — para consumo das APIs
  - `datetime` — para registrar data/hora das consultas

---

## 🚀 Funcionalidades

1. Exibe mensagem de início do programa  
2. Obtém localização automática via API de IP  
3. Confirma a cidade detectada com o usuário  
4. Consulta a API do OpenWeatherMap para obter dados climáticos  
5. Exibe as informações formatadas no terminal  
6. Salva as consultas no arquivo `consultas.txt`

---

## 🔑 Requisitos

- Ter o **Python 3.8+** instalado  
- Instalar a biblioteca `requests`:
  ```bash
  pip install requests
