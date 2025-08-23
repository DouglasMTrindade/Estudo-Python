def le_valores_lista (quantidade):
    """ 
    Le uma quantidade fixa de valores e retorna esses uma lista composta com valores pares e impares ordenados
    
    retorno:
    lista_valores[lista] - lista composta onde:
        - lista_valores[0] números pares
        - lista_valores[1] números ímpares
    """
    lista_valores = [[],[]]
    for n in range(quantidade):
        while True:
            entrada = input (f"Digite o {n+1}º valor: ")
            try:
                entrada = int(entrada)
                break
            except ValueError:
                print ("Valor digitado inválido. Digite novamente.")

        if entrada%2 ==0: 
            lista_valores[0].append(entrada)
        else: 
            lista_valores[1].append(entrada)

    #ordena  numeros pares e ímpares
    lista_valores[0].sort()
    lista_valores[1].sort()

    return lista_valores

#Programa principal
quantidade = 7 # quantidade de valores que vai ser lida

print("Lista de pares e ímpares")
print(f"Digite {quantidade} números")

lista = le_valores_lista(quantidade)

#Exibe resultados
print(f"Valores pares: {lista[0]}")
print(f"Valores impares: {lista[1]}")