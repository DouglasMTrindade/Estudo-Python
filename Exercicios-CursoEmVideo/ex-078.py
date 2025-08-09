#Entrada de valores e cria uma lista
lista_valores = [int(input(f'Digite o {i+1}º valor:')) for i in range(5)]

#Classifica o menor e maior valor da lista
menor = min(lista_valores)
maior = max(lista_valores)

#Lista a posição do menor e maior valor da lista
posicao_menor = [ i for i, v in enumerate(lista_valores) if v == menor]
posicao_maior = [ i for i,v in enumerate(lista_valores) if v == maior]

#Exibe os resultados encontrados
print (lista_valores)
print (f'Menor valor da lista: {menor}')
print (f'Menor valor na posição: {posicao_menor}')
print (f'Maior valor da lista: {maior}')
print (f'Maior valor na posição: {posicao_maior}')