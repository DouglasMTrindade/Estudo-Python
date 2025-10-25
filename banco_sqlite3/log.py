import os
import json


def salva_log (local, clima,agora):
    dados = []

    linha = f'[{agora}] {local} {clima} \n'

    try:
        with open ('log.tex','a',encoding='utf-8') as f:
            f.write(linha)
    except FileNotFoundError:
        print("Arquivo não existe")
    except PermissionError:
        print("Sem permissão")
    except OSError as e:
        print("ERRO de IO: ",e)

    if os.path.exists('log.json'):
        with open ('log.json', 'r', encoding='utf-8') as arquivo:
            try:
                registro = json.load(arquivo)
            except json.JSONDecodeError:
                print("Arquivo vazio ou corrompidos, iniciando lista nova.")
                registro =[]
    else:
        print("arquivo não encontrado, criando novo")
        registro = []

    dados = {
        'Consulta': agora,
        'Cidade': local['cidade'],
        'loc': local['loc'],
        'Clima':
        {
            'temperatura': clima['temperatura'], 'sensação': clima['sensacao_termica'],'vento': clima['vento'],'descrição': clima['descricao']
        }       
    }
    registro.append(dados)

    with open ('log.json','w',encoding='utf-8') as reg:
        json.dump(registro,reg,ensure_ascii=False, ident=2)