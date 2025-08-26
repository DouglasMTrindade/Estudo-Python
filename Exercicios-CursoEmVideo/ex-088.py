import random
import time
def sorteia_numeros_mega_sena ():
    """
    le quantidade de jogos e gera combinaçoes da Mega Sena

    Retorna:
        Jogos : lista composta com seis numeros aleatorios ordenados de 1 a 60
        quantidade: numero de jogos fornecido pelo usuario
    """
    
    while True:
        try:
            quantidade = int(input("Quantos jogos deseja sortear ? "))
            break
        except ValueError:
            print ("Valor digidado inválido, Digite novamente!")
    
    jogos = []
    jogos =[sorted(random.sample(range(1,60), 6)) for _ in range(quantidade)]


    return jogos, quantidade

# Programa principal
print("-"*30)
print(f"{'JOGA NA MEGA SENA':^30}")
print("-"*30)
jogos, quantidade = sorteia_numeros_mega_sena()


#Exibe Resultados
print("-="*3, f" Sorteando {quantidade} Jogos", "-="*3)
for c, linha  in enumerate(jogos, start=1):
    time.sleep(1.5)
    print(f"Jogo {c} : ",linha)