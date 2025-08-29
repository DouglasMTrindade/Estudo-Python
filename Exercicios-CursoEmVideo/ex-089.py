def le_boletim ():
    """
    Lê nome de aluno e notas ate que seja digitado 'sair' ou pressionado Enter.
    Retorna:
        boletim: lista de alunos no formato[[nome,nota1,nota2,media],...]
    """
    boletim = []
    print("Cadastro de alunos.(Enter ou 'sair' encerra)")
    while True:
        nome = (input("Nome: ")).strip()
        if nome.lower() == 'sair' or nome == '':
            break
        
        nota1 = le_float('Nota 1: ')
        nota2 = le_float('Nota 2: ')

        media = (nota1+nota2)/2
        entrada = [nome.title(),nota1,nota2,media]
        boletim.append(entrada)
        
        
    return boletim

def le_float(mensagem):
    """
    Lê um valor do tipo float fornecido pelo usuario
    Retorna:
        float - valor digitado pelo usuario
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um numero válido")


def visualiza_nota (boletim):
    """
    Permite ao usuário consultar as notas de um aluno pelo indice
    Retorna:
        none - exibe os nome e notas na tela
    """
    if not boletim:
         print("Nenhum aluno cadastrado")
         return

    while True:
        
        entrada = input("Gostaria de ver a nota de qual aluno('sair' encerra): ").strip()
        if entrada.lower() == 'sair' or entrada == '':
            break

        try:
            indice = int(entrada)
        except ValueError:
            print ("Entrada inválida! Digite um numero de aluno valido ou 'sair'")
            continue

        if 0 <= indice < len(boletim):
            notas = boletim[indice][1:3]
            print(f"Notas de {boletim[indice][0]} são {notas}", end = "\n\n")
        else:
            print(f"Número inválido!")

        
def imprime_boletim (boletim):
    """
    Exibe o boletim completo com indices, nome e media formatados
    Retorna:
        none - exibe resultados na tela
    """
    print(f"{'No.':<4}{'NOME':<20}MEDIA")
    print("-"*30)
    for c, pessoas in enumerate(boletim, start=0):
        print (f"{c:<4}{pessoas[0]:<20}{pessoas[3]:>5.1f}")
    print("-="*40)


#Programa principal
boletim = le_boletim()
imprime_boletim(boletim)
visualiza_nota(boletim)