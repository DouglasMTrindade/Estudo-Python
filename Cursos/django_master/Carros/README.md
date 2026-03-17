# Sistema de Cadastro de Carros

Este projeto é uma aplicação web feita com Django para gerenciar carros. Ele permite que usuários se cadastrem, façam login, adicionem carros, editem, excluam, visualizem detalhes e façam upload de fotos. Também há uma integração com inteligência artificial para gerar uma bio automática para cada carro.

## Como usar

1. Instale as dependências com o comando:
   ```
   pip install -r requirements.txt
   ```
2. Configure o banco de dados no arquivo .env ou diretamente no settings.py.
3. Rode as migrações:
   ```
   python manage.py migrate
   ```
4. Crie um superusuário:
   ```
   python manage.py createsuperuser
   ```
5. Inicie o servidor:
   ```
   python manage.py runserver
   ```
6. Acesse o sistema pelo navegador em http://localhost:8000

## Funcionalidades

- Cadastro e login de usuários
- Cadastro, edição, exclusão e listagem de carros
- Upload de fotos dos carros
- Visualização dos detalhes de cada carro
- Geração automática de bio para o carro usando IA
- Interface simples

## Estrutura

- A pasta accounts cuida do cadastro e autenticação de usuários.
- A pasta cars gerencia os carros, formulários, templates e integrações.
- A pasta geminai_api faz a comunicação com a IA para gerar a bio.
- A pasta media armazena as fotos enviadas.
- O arquivo requirements.txt lista as dependências do projeto.

## Observações

- Para usar a geração de bio, é preciso configurar a chave da API da IA.
- O projeto usa PostgreSQL, mas pode ser adaptado para outros bancos.
- O sistema é voltado para fins de estudo e prática com Django.
