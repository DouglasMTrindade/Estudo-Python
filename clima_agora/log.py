from datetime import datetime
import os
import json

def salva_consulta (local, clima):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    linha = f'[{agora}] {local} {clima} \n'
    registro = {
        'Consulta': agora,
        'Cidade': local['cidade'],
        'loc': local['loc'],
        'Clima':
        {'temperatura': clima['temperatura'], 'sensacao': clima['sensacao_termica'], 'vento': clima['vento'], 'descricao': clima['descricao']
         }
    }

    try:        
        with open ('log.txt','a',encoding='utf-8') as f:
            f.write(linha)
  
        with open ('registro.json','a',encoding='utf-8') as reg:
            json.dump(registro,reg,ensure_ascii=False,indent=2)
            reg.write('\n')
    except FileNotFoundError:
        print('Arquivo não existe')
    except PermissionError:
        print("Sem permissão")
    except OSError as e:
        print("Erro de IO:",e)