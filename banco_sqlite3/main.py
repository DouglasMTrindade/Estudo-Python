from localizacao import busca_localizacao
from clima import clima_agora
from log import salva_log
import clima_historico

if __name__ == '__main__':
    print("--Buscando localizacao--")
    local = busca_localizacao()
    if local:
        clima, agora = clima_agora(local)
    else:
        clima,agora = None
    print(local,clima,agora)

    if local and clima:
        clima_historico.cria_tabela()
        clima_historico.salva_consulta(local, clima,agora)
        clima_historico.lista_consultas()
        clima_historico.filtrar_por_cidade('Canoas')
