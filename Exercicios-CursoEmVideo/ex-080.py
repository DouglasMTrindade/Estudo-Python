def le_valores_lista (qtd):
#Lê 'qtd' de numeros inteiros, sem repetições e mantem a lista ordenada sem a uliziacao de '.sort()'.
    valores = []
    cont = 0
    while cont < qtd:
        entrada = input(f"Informe o {cont+1}º numero:")

        try:
            numero = int(entrada)
            #Evita valores duplicados na lista
            if numero in valores:
                print ("Numero digitado já esta na lista, digite novamente")
            else:
                #Posiciona o numero corretamente na lista
                posicao = 0 
                while posicao < len(valores) and numero > valores[posicao]:
                    posicao += 1
                #Insere o numero na posiçao correta da lista
                valores.insert(posicao,numero)
                cont += 1
        #Tratamento de erro na conversao para inteiro
        except ValueError:
            print ("Valor digitado invalido")
            
    return valores

#Executa o programa
lista_valores = le_valores_lista(5)

#Exibe os resultados
print("Lista de valores ordenada: ",lista_valores)