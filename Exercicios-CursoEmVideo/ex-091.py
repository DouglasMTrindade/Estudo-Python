import random 
import time

def sorteia_numero(quantidade):
    """
    Sorteira numeros inteiros para cada jogador

    recebe:
        quantidade(int) - número de jogadores
    Retorna:
        Sorteio - dicionario com numeros sorteados para cada jogador
    """
    sorteio ={}
    print("Valores Sorteados:", end = '\n\n')
    for c in range(quantidade):
        valor = random.randint(1, 20)
        sorteio[f'jogador{c+1}'] = valor
        print(f"jogador{c+1} tirou  {valor} no dado")
    return sorteio


def ranking(sorteio):
    """
    Ordena dicionario do sorteio pelo valor sorteado e imprime de maior para menor numero
    Recebe:
        Sorteio(dict) - dicionario de jogadores e valores 
    Retorna:
        None - imprime na tela Ranking ordenado do maior para o menor valor ordenado
    """
    ranking_ordenado = dict(sorted(sorteio.items(), key=lambda x:x[1], reverse =True))
    print('== RANKING DOS JOGADORES ==')
    for posicao ,(jogador, valor) in enumerate(ranking_ordenado.items(), start=1):
        time.sleep(1)
        print (f" {posicao}º lugar: {jogador} com {valor}")
        

#Programa principal
quantidade_jogadores = 4
sorteio = sorteia_numero(quantidade_jogadores)
print("-="*30)
ranking(sorteio)
