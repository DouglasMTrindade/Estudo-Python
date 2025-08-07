import random

#Recebe valores inteiros digitados e salva em uma tupla
numeros= tuple(int(input(f"digite o {i+1}º numero: ")) for i in range(5))

#zera contadores
cont9 = 0
cont3 = 0
contpar =0

#Verifica os valores salvos na tupla
for valor in numeros:
    if valor == 9:
        cont9 += 1
    elif valor == 3 and cont3 != 1:
        cont3 += 1
    elif valor%2 == 0:
        contpar += 1
    

#Exibe os resultados
print (f"Numeros digitados: {numeros}")
print (f"Quantida de digitos 9: {cont9}")
print (f"Posiçao do primeiro digito 3: {cont3}")
print (f"Quantidade numeros pares: {contpar}")