from time import sleep

def contador(inicio, fim, passo):
    """
    Faz contagem com base no inici, fim e passo informados
    Recebe:
        inicio(int): valor de inicio da contagem
        fim(int): valor final da contagem
        passo(int): valor de passo da contagem
    Retorna:
        None: exibe a contagem na tela
    """
    contador = inicio
    passo = abs(passo)

    print("-="*30)
    print(f"contagem de {inicio} ate {fim} de {passo} a {passo}")

    if inicio < fim:
        while contador <= fim:
            print(f"{contador} ",end='', flush=True)
            sleep(0.5)
            contador += passo
    else:
        while contador >= fim:
            print(f"{contador} ", end='', flush=True)
            sleep(0.5)
            contador -= passo
    print("Fim")
    print("-="*30)


def le_int(mensagem):
    """
    le numero digitado pelo usuario repete ate que seja valido
    Recebe:
        mensagem(str):texto que sera exibido para o usuario
    Retorna:
        int: número inteiro digitado valido
    """

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor digitado inválido")


def dados_contador():
    """
    Lê valores digitados pelo usuaro para inicio, fim e passo da contagem
    Permite encerrar digitando 999
    Retorna:
        None - chama funcao para exiber dados na tela
    """
    print("Personalize a contagem (999 encerra)")
    while True:
        inicio = le_int('Inicio: ')
        if inicio == 999:
            break

        fim = le_int('Fim: ')
        if fim == 999:
            break

        passo = le_int('Passo: ')
        if passo == 999:
            break
        elif passo == 0:
            passo = 1
            print("Passo invalido, considerado passo = 1")

        contador(inicio,fim,passo)
#programa principal
print("Contador Personalizavel")
contador(1,10,1)
contador(10,0,1)
dados_contador()

print(">>>ENCERRADO<<<")




