import random 

# Sorteia 5 numeros entre 0 e 10
numeros_sorteados= tuple(random.randint(0,10) for _ in range(5))

#Exibe resultados
print (f"numeros sorteados: {numeros_sorteados}")
print (f"Menor Valor :{min(numeros_sorteados)}")
print (f"Maior Valor :{max(numeros_sorteados)}")