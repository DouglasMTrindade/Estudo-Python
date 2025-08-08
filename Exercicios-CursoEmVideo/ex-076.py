lista_produtos = (
    "Ovo",17.90,
    "Patinho",39.90,
    "Arroz",13.98
    )

for indice in range(0, len(lista_produtos), 2):
    produto = lista_produtos[indice]
    valor = lista_produtos[indice+1]
    print (f"{produto:.<20} R${valor:>6.2f}")