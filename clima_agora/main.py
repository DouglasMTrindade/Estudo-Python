from localizacao import busca_localizacao
from clima import busca_clima

if __name__ == '__main__':
    print("---Iniciando busca de localização---")
    dados_local = busca_localizacao()

    if dados_local:
        print(dados_local['cidade'])
        print(dados_local['loc'])
    else:
        print("Não foi possivel obter a localizacao")

    previsao = busca_clima(dados_local['loc'])

    print(previsao)

print("---FIM---")