def le_boletim_medias():
    """
    Cadastro de media de alunos e suas situações 
    Recebe nome do aluno e sua media informados pelo usuario, e calcula a situação de cada um.
    Retorna:
        boletim_media:dicionario com os dados dos alunos.
    
    """
    boletim_media ={}
    while True:
    
        aluno = input("Digite o nome do aluno: ").strip()
        if aluno.lower() == 'sair' or aluno == '':
            break

        media= le_float(f'digite a media de {aluno.title()}: ')

        if media >= 7 :
            situacao = 'Aprovado'
        elif media >= 5:
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'

        boletim_media[aluno]={
            'media': media ,
            'situacao': situacao
            }
        imprime_boletim_individual(boletim_media[aluno], aluno)

    return boletim_media


def le_float(mensagem):
    """"
    Lê um valor digitado pelo usuario e garante que é um valor numerico valido(float)
    Retorna:
        valor valido (float)
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor digitado invalido, digite novamente")


def imprime_boletim_individual(boletim_individual, aluno):
    """
    Recebe a media, situacao e nome do aluno que foi cadastrado
    Retorna:
        - Exibe na tela nome, media e situacao do aluno formatado
    """

    print("-="*30)
    print(f"NOME: {aluno.title()}")
    print(f"MEDIA: {boletim_individual['media']}")
    print(f"SITUACAO: {boletim_individual['situacao']}", end ='\n\n')


def imprime_boletins(boletim_medias):
    """
    Recebe o boletim com todos os cadastro criados e imprime completo 
    Retorno:
        -Exibe na tela nome, media e situcao de todos os alunos de uma vez formatado
    """
    
    print("-="*30)
    if not boletim_medias:
        print("Nenhum cadatro realizado")
    else:
        print(f"{'NOME':<20}{'MEDIA':<7}{'SITUACAO'}")
        for nome, dados in boletim_medias.items():
            print(f"{nome.title():<20}{dados['media']:<7}{dados['situacao']}")
        print("-="*30)


#Programa pricipal
print("-="*30)
print("Cadastro de medias de alunos")
print("-="*30)

boletim_medias =le_boletim_medias()

imprime_boletins(boletim_medias)

print("programa encerrado")