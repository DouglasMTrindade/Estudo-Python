def le_valores_lista():
    #Lê valores e adiciona em ordem em uma lista até que seja digitado 'sair'
    lista_valores =[]

    while True:
        entrada = input(f"Digite o {len(lista_valores)+1}º (ou 'sair' para finalizar): ")

        if entrada.lower() == 'sair':
            break

        try:
            valor= int(entrada)
            posicao = 0
            while posicao < len(lista_valores) and valor > lista_valores[posicao]:
                posicao += 1
            lista_valores.insert(posicao, valor)
        except ValueError:
            print ("Valor digitado invalido, digite novamente.")

    return lista_valores


def analisa_lista(lista):
    #Separa os valores pares e impares e salva em uma lista
    par=[i for i in lista if i % 2 ==0]
    impar = [i for i in lista if i % 2 != 0]
    
    return par, impar

#executa o progrma
lista_valores = le_valores_lista()
lista_par, lista_impar = analisa_lista(lista_valores)

#Exibe o resultado
print (f"Lista digitada: {lista_valores}")
print(f"Lista de valore par: {lista_par}")
print (f"Lista de valores impares: {lista_impar}")