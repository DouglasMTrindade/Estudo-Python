from time import sleep
from random import sample

def maior(valores):
    """
    Analisa uma lista de valores e informa o maior valor, quantidade de valores na lista e imprime alista
    Args:
        - valores(list) : lista de valores para analisar

    Returns:
        - None : Apenas exibe na tela de forma formatada
    """

    print("-="*30)   
    if valores:
        maior_valor = max(valores)
        print("Analisando valores passados ...")
        for numeros in valores:
            print(f"{numeros} ",end='',flush=True)
            sleep(0.5)
        print(f"Foram informados {len(valores)} valores ao todo.")
        print(f"Maior valor informado foi: {maior_valor}")
    else:
        print("Nenhum valor informado")

    print("-="*30)


def le_int(mensagem):
    """
    Le valor inteiro digitado pelo usuario ou '' sem valor
    Args:
        - mensagem(str) - mensagem que sera mostrada ao usuario
    Returns:
        - int | None : número interio válido ou None se o usuário nao digitou nada
    """
    while True:
        valor = input(mensagem)
        if valor == '':
            return None
        try:
            return int(valor)
        except ValueError:
            print("Valor Inválido, Digite novamente")


def sorteia_numeros():
    """
    Le valores digitados pelo usuario e sorteia uma lista de valores.
    Args:
        -None
    Returns:
        -None
    
    """
    print("sorteia numeros inteiros")
    while True:
        quantidade = le_int('Quantos numeros: ')
        if quantidade == 999 or quantidade is None:
            break

        inicio = le_int('Menor valor: ')
        if inicio == 999 or inicio is None:
            break
        
        fim = le_int('Maior valor:')
        if fim == 999 or fim is None:
            break

        
        if inicio > fim:
            inicio,fim = fim, inicio

        if 0< quantidade <= (fim - inicio + 1):
            valores = sample(range(inicio, fim+1),quantidade)
            maior(valores)
        else:
            print("Range digitado inválido")


def le_numeros():
    """
    lê valores inteiros digitados pelo usuario e salva em uma lista
    Args:
        - None
    Returns:
        - None
    """
    repete = True
    while repete:
        lista_valores = []
        cont = 1
        print("Digite os valores a analisar (Enter ou 999 encerra)")
        while True:
            numero = le_int(f'{cont}° numero: ')
            if numero == 999 or numero is None:
                break
            lista_valores.append(numero)
            cont += 1
        if lista_valores:
            maior(lista_valores)
        else:
            print('Nenhum valor digitado')
        
        while True:
            continua = input('Deseja continuar [S/N]').strip().upper()
            if continua == 'S':
                break
            elif continua == 'N':
                repete = False
                break
            else:
                print("Valor digitado invalido. Digite novamente")



#Programa principal
maior([1,2,3,4])
sorteia_numeros()
le_numeros()