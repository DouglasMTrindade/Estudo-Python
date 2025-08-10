def le_valores_lista():
    #Lê valores e adiciona em uma lista ate que seja digitado 'sair'
    lista_numeros = []
    while True:
        entrada = input(f"digite o valor o {len(lista_numeros)+1}º valor: (ou 'sair' para fechar)")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            numero = int(entrada)
            lista_numeros.append(numero)
        except ValueError:
            print ("Valor digitado invalido, digite novamente.")
    return lista_numeros

def analisa_lista (lista):
    #Le a lista e verifica se o valor 5 esta presente, e returna suas posicoes
    if 5 in lista:
        posicoes = [i +1 for i, valor in enumerate(lista) if valor == 5]
        return f'O valor 5 aparece na posicao {posicoes} da lista'
    else:
        return 'O valor 5 nao aparece na lista'

    
#Executa o programa
lista = le_valores_lista()
mensagem_valor5 = analisa_lista(lista)

#Exibe os resultados
print(f"Foram digitados {len(lista)} valores")
print("Valores salvos na lista:", lista)
print (mensagem_valor5)