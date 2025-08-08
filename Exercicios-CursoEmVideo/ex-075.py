#Recebe valores inteiros digitados e salva em uma tupla
numeros= tuple(int(input(f"digite o {i+1}º numero: ")) for i in range(4))


#Verifica os valores salvos na tupla
conta9 = numeros.count(9)
numeros_par = [valor for valor in numeros if valor%2 ==0]

#Verifica a posição do número 3
try:
    indice_3 = numeros.index(3)
    mensagem_3 = f"O número 3 aparece na posiçao {indice_3} da tupla"
except ValueError:
    mensagem_3 = "Não contem o numero 3"


#Exibe os resultados
print (f"Números digitados: {numeros}")
print (f"Quantidade de vezes que o numero 9 apareceu: {conta9}")
print (mensagem_3)

if numeros_par:
    print (f"Números pares: {numeros_par}")
else:
    print ("Não contem numeros pares")