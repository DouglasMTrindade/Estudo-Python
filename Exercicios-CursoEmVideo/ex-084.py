def le_valores_lista ():
    # le Nome e peso e retorna uma lista composta [[nome,peso],...]
    lista = []
    while True:
        nome = input("Nome: ")
        if nome.lower() == 'sair':
            break
           
        peso = input("Peso: ")
        if peso.lower() == 'sair':
            break

        try:
            peso = float(peso)      
            lista.append([nome,peso])                 
        except ValueError:
            print ("Valor digitado Invalido, digite novamente")
        


    return lista

def verifica_lista(lista):
    #Retorna maior/menor peso e as pessoas com esses valore.
    maior_peso = max(p[1] for p in lista)
    mais_pesados = [p[0] for p in lista if p[1] == maior_peso]

    menor_peso = min(p[1] for p in lista)
    mais_leves = [p[0] for p in lista if p[1] == menor_peso]

    return maior_peso,menor_peso,mais_pesados,mais_leves


#Programa principal
print ("Digite o nome e peso para salvar: (ou 'sair' para encerrar)")
lista_completa = le_valores_lista()

if lista_completa: # So analisa se tiver valores na lista
    maior_peso, menor_peso, mais_pesados, mais_leves = verifica_lista(lista_completa)

    print (f"O maior peso foi de {maior_peso}, peso de {mais_pesados}")
    print (f"O menor peso foi de {menor_peso}, peso de {mais_leves}")
else:
    print("Nenhum dado valido digitado")