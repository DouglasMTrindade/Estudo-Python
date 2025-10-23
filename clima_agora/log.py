from datetime import datetime
import os
import json

def salva_consulta (local, clima):
    dados = []
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    linha = f'[{agora}] {local} {clima} \n'
    
    try:        
        with open ('log.txt','a',encoding='utf-8') as f:
            f.write(linha)
  
    except FileNotFoundError:
        print('Arquivo não existe')
    except PermissionError:
        print("Sem permissão")
    except OSError as e:
        print("Erro de IO:",e)


    if os.path.exists('log.json'):
        with open ('log.json','r',encoding='utf-8') as arquivo:
            try:
                registro = json.load(arquivo)
            except json.JSONDecodeError:
                print("Arquivo vazio ou corrompidos, iniciando lista nova.")
                registro = []
    else:
        print("Arquivo não encontrado, criando novo")
        registro = []

    dados = {
        'Consulta': agora,
        'Cidade': local['cidade'],
        'loc': local['loc'],
        'Clima':
        {'temperatura': clima['temperatura'], 'sensacao': clima['sensacao_termica'], 'vento': clima['vento'], 'descricao': clima['descricao']
         }
    }
    registro.append(dados)

    with open ('log.json','w',encoding='utf-8') as reg:
        json.dump(registro,reg,ensure_ascii=False,indent=2)
