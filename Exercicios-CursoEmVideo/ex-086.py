def le_valores_matriz (linha, coluna):
    """
    Lê valores interiros fornecidos pelo usuário e retorna uma matriz.

    Retorna:
        matriz: matriz preenchida com valores inteiros
    """
    matriz = []

    for n in range(linha):
        linha_atual = []
        for i in range(coluna):

            while True:
                entrada = input (f"Digite o valor [{n},{i}]: ")
                try:
                    entrada = int(entrada)
                    break
                except ValueError:
                    print("Valor digitado inválido. Digite novamente.")
            linha_atual.append(entrada)

        matriz.append(linha_atual)

    return matriz


#programa principal
linha = 3
coluna =3
matriz = le_valores_matriz(linha, coluna)

#exibe resultado organizado 
for linha_atual in matriz:
    for n in linha_atual:
        print(f"[{n:^5}]" ,end ="")
    print("")