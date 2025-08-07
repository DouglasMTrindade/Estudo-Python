import random 


sorteio = [random.randint(0,10) for _ in range(6)]
tupla_sorteio = tuple(sorteio)
print(f"numeros sorteados: {tupla_sorteio}")
print (f"Menor Valor :{min(tupla_sorteio)}")
print (f"Maior Valor :{max(tupla_sorteio)}")