def le_valores_matriz (linha, coluna):
    """
    Le valores inteiros fornecidos pelo usuario

    Retorna:
        Matriz : preenchida com numeros inteiros 
    """
    matriz = []

    for l in range(linha):
        linha_atual = []
        for n in range(coluna):
            while True:
                entrada = input(f"Digite o valor [{l},{n}]: ")
                try:
                    entrada = int(entrada)
                    break
                except ValueError:
                    print("Valor digitado inválido, Digite novamente.")
            linha_atual.append(entrada)
        matriz.append(linha_atual)
    
    return matriz

def analisa_matriz (matriz):
    """
    verifica a matriz gerada pelo usuario

    Retorna:
        -Soma dos valores pares
        -Soma da terceira coluna
        -Soma da segunda linha
        -largura para formatação de exibicao da matriz
    """

    soma_par = 0
    maior_valor = 0
    soma_coluna3 = 0
    soma_linha2 = 0
    for linha in matriz:
        for valor in linha:
            if valor%2 ==0:
                soma_par += valor
            if valor > maior_valor:
                maior_valor = valor

        if len(linha) >= 3:
            soma_coluna3 += linha[2]
    soma_linha2 = sum(matriz[1])
    largura = len(str(maior_valor))

    return soma_par,largura, soma_coluna3, soma_linha2
        


#Programa principal
linha, coluna = 3, 3
matriz = le_valores_matriz(linha, coluna)
soma_par, largura, soma_coluna3, soma_linha2 = analisa_matriz(matriz)


#exibe resultados
for linhas in matriz:
    for colunas in linhas:
        print(f"[{colunas:^{largura}}]" ,end =" ")
    print("")

print("Soma de valores pares da matriz: ",soma_par)
print("Soma dos valores da 3ª coluna: ",soma_coluna3)
print("Soma dos valores da 2ª linha",soma_linha2)