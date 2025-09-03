def cadastro_pessoas():
    """
    Cadastro de pessoas usuario informa nome, sexo e idade
    Retorna:
        cadastro(list) : [{nome,sexo e idade},...]
    """

    print("Cadastro, digite as informacoes('sair ou Enter para encerrar)")
    cadastro = []
    while True:
        entrada ={}
        
        nome = input('Nome: ')
        if nome.lower() == 'sair' or nome == '':
            break

        while True:
            sexo = input("Sexo [M/F]: ").lower()
            if sexo == 'sair' or sexo == '':
                return cadastro
            elif sexo == 'm' or sexo =='f':
                break
            else:
                print("Valor digitado incorreto")

        while True:
            idade = (input("Idade: "))
            if idade.lower() == 'sair' or idade == '':
                return cadastro
            try:
                idade = int(idade)
                break
            except ValueError:
                print("Valor digitado inválido, digite novamente")
        entrada = {
            'nome': nome.strip().capitalize(),
            'sexo': sexo,
            'idade':idade
        }

        cadastro.append(entrada)
        print()
    
    return cadastro


def imprime_cadastro(cadastro):
    """
    Exibe informacoes do cadastro formatadas
    Calcula:
        -media de idade
        -numero de cadastros
    Mostra:
        -numero de cadastros
        -media de idade
        -mulheres cadastras
        -pessoas acima da media de idade
    Retorna:
        None
    """
    print("-="*30)
    numero_cadastros = len(cadastro)
    if numero_cadastros <= 0:
        print("Nenhum dado cadastrado")
        return
    print(f"Ao todo temos {numero_cadastros} cadastradas")

    soma_idade = 0
    mulheres = []
    for pessoa in cadastro:
        soma_idade = soma_idade+pessoa['idade']
        if pessoa['sexo'] == 'f':
            mulheres.append(pessoa['nome'])
    
    media_idades = soma_idade/numero_cadastros

    print(f"A media de idade é de {media_idades:.1f}")
    if mulheres:
        print(f"As mulheres cadastras na lista foram: {', '.join(mulheres)}")
    else:
        print("Nenhuma mulher cadastrada")
    print("Lista das pessoas que estão acima da media:")

    for pessoa in cadastro:
        if pessoa['idade'] > media_idades:
            print(f"   Nome : {pessoa['nome'].title()}; Idade : {pessoa['idade']}; Sexo : {pessoa['sexo'].upper()}")

    




#programa principal
cadastro = cadastro_pessoas()
imprime_cadastro(cadastro)

print(">>>Encerrado<<<")