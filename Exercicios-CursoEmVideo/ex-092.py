from datetime import date


def cadastro_trabalhador():
    """
    Cadastro de trabalhador dados pessoais e previdenciarios

    Retorno:
        Cadastro(dict)- com dados do trabalhador
    """
    data_atual = date.today().year
    cadastro ={}

    cadastro['nome'] = input("Nome: ").strip().title()
    nascimento = le_int('Ano de nascimento: ')
    
    
    idade = data_atual - nascimento
    cadastro['idade']  = idade
    carteira = le_int('Carteira de trabalho (0 não tem)')
    cadastro['carteira trabalho'] = carteira 

    if cadastro['carteira trabalho'] > 0:
        contratacao= le_int('Ano de contratação: ')
        salario = le_float('Salario: ')
        
        cadastro['contrataçao: '] = contratacao
        cadastro['salario'] = salario

        idade_aposentadoria = idade +(35-(data_atual - contratacao))
        cadastro['aposentadoria'] = idade_aposentadoria
    return cadastro


def imprime_cadastro(cadastro):
    """
    Exibe na tela as informacoes do trabalhador de forma formatada
    Recebe:
        cadastro(dict)- dicionario com dados do trabalhador
    Retorna:
        None - exibe o resultado na tela
    """
    print("-="*30)
    for info, valor in cadastro.items():
        print(f"{info.title():<20}: {valor}")
    

def le_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            break
        except ValueError:
            print("Valor digitado inválido. Dgite novamente")
    return valor


def le_int(mensagem):
    while True:
        try:
            valor= int(input(mensagem))
            break
        except ValueError:
            print("Valor digitado inválido. Digite novamente")
    return valor


#Programa principal
cadastro=cadastro_trabalhador()
imprime_cadastro(cadastro)