# Projeto: Consulta de Clima com Localização Automática

Este projeto em **Python** consulta informações climáticas atuais usando a **API do OpenWeatherMap** 🌤️.  
A localização do usuário é identificada automaticamente por meio da **API do IPinfo**, que fornece dados de cidade e coordenadas (latitude e longitude).  
Com base nisso, o programa exibe informações sobre:


- Localização detectada  
- Temperatura atual  
- Sensação térmica  
- Velocidade do vento  
- Condição do tempo  

Além disso,todas as consultas realizadas são registradas nos arquivo `log.txt` e `log.json`.

---

## Objetivo

Este é um projeto de **aprendizado**, desenvolvido para praticar:
- Consumo de **APIs REST** com Python (`requests`, `json`)
- Manipulação de dados retornados em formato **JSON** e **TXT**
- Estruturação modular de código
- Uso de **variáveis de ambiente** para proteger chaves de API  
- Escrita e leitura de **arquivos de log**
- Boas práticas de programação e documentação

---

## Tecnologias utilizadas

- **Python 3.x**
- **Bibliotecas:**
  - `requests` — para consumo das APIs
  - `datetime` — para registrar data/hora das consultas
  - `json` → para manipulação dos registros em arquivo  
  - `os` → para verificação e criação de arquivos  
  - `dotenv` → para carregar variáveis do arquivo `.env`


---

## Funcionalidades

1. Exibe mensagem de início do programa  
2. Obtém localização automática via API de IP  
3. Consulta a API do OpenWeatherMap para obter dados climáticos  
4. Exibe as informações formatadas no terminal  
  - Temperatura atual
   - Sensação térmica
   - Velocidade do vento
   - Condição do tempo
5. Salva o histórico de consultas em:
   - `log.txt` (texto)
   - `log.json` (formato estruturado)
6. Realiza tratamento de erros para:
   - Falhas na requisição das APIs  
   - Chaves de API ausentes  
   - Arquivo JSON vazio ou corrompido  

---

## 🔑 Requisitos

- Ter o **Python 3.8+** instalado  
- Instalar a biblioteca `requests`:
  ```bash
  pip install requests
