from localizacao import busca_localizacao
from clima import clima_agora
from log import salva_log
from valida_entrada import menu
import clima_historico

if __name__ == '__main__':
    clima_historico.cria_tabela()

    while True:
        opcao = menu()

        if opcao == 0:
            opcao = menu()
        elif opcao == 1:
            local = busca_localizacao()
            if local:
                clima, agora = clima_agora(local)
                if clima and agora:
                    clima_historico.salva_consulta(local,clima, agora)
                    print(clima, agora)
            else:
                clima, agora = None, None
            
        elif opcao == 2:
            clima_historico.lista_consultas()
        elif opcao == 3:
            clima_historico.filtrar_por_cidade()
        elif opcao == 4:
            clima_historico.apagar_por_id()
        elif opcao == 5:
            break
        else:
            print(f"Opcao {opcao}, Inválida")
            opcao = 0


'''
    if local and clima:
        clima_historico.cria_tabela()
        clima_historico.salva_consulta(local, clima,agora)
        clima_historico.lista_consultas()
        clima_historico.filtrar_por_cidade('Porto Alegre')
        clima_historico.apagar_por_id()
'''
