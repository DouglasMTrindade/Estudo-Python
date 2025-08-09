def ler_valores_lista ():
    #Entrada valores inteiros ate que seja digitado 'sair'
    valores = []
    while True:
        entrada = input("Digite um valor ('sair' para encerrar a entrada):")

        #Aceita 'sair' em maiúscula/minúscula
        if entrada.lower() == 'sair': 
            break

        #Verifica se o valor digita e um inteiro e se ja esta na lista
        try:
            numero = int(entrada)
            if numero in valores:
               print ("Valor já está na lista! Digite outro")
            else:
                valores.append(numero)
        except ValueError:
           print("valor digitado inválido! Digite um número inteiro ou 'sair'")

    return valores


#Entrada de valores utilizando a função
lista_valores = ler_valores_lista()
lista_valores.sort()

#Exibe o resultado
print(lista_valores)