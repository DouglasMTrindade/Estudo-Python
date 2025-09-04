def cadastro_jogador():
    """
    Cadastro de jogador nome e dados das partidas jogadas

    Retorna:
        cadastro(dict):{nome, partidas, gols, total}
    """
    cadastro ={}
    while True:
        nome = input("Nome: ").strip().capitalize()
        if nome != '':
            break
        else:
            print("Digite o nome")

    cadastro['nome'] = nome
    partidas = le_int('Partidas: ')
    cadastro['partidas'] = partidas

    gols =[]
    for c in range(partidas):
        gols.append(le_int(f"gols na {c+1}º partida: "))

    cadastro['gols'] = gols
    cadastro['total'] = sum(gols)

    print("-="*30)
    print(cadastro)

    return cadastro


def multi_cadastro_jogadores():
    """
    Salva cadastro de jogador em uma lista até que o usuario parar

    Retorna:
        -cadastro_jogadores(list)- [{nome, partidas, gols, total},...]
    """
    cadastro_jogadores =[]
    while True:
        jogador = cadastro_jogador()
        cadastro_jogadores.append(jogador)
        while True:
            continua = input("Deseja continuar [S/N]: ").strip().lower()
            if continua == 'n':
                return cadastro_jogadores
            elif continua == 's':
                break
            else:
                print("valor invalido digitado")


def imprime_cadastro(cadastro_jogadores):
    """
    Imprime o cadastro dos jogadores realizados
    Recebe:
        Cadastro(lista) - lista com dados do jogador cadastrado
    Retorna:
        None - imprime cadastro formatado na tela com indice
    """
    print("-="*30)

    print(f"Cod {'Nome':<20}{'Gols':<20}Total")
    for indice,cadastro in enumerate(cadastro_jogadores , start=0):
        gols = cadastro['gols']
        print(f"{indice:>3} {cadastro['nome']:<20}{str(cadastro['gols']):<20}{cadastro['total']}")
        #for chave, valor in cadastro.items():
        #    print(f"{chave.capitalize():<12}: {valor}")
    print("-="*30)


def imprime_gols(cadastro_jogadores, indice):
    """
    Imprime o cadastro do jogador realizado
    Recebe:
        Cadastro(lista) - lista com dados do jogador cadastrado
        Indice(int) - valor da lista que sera impresso
    Retorna:
        None - imprime cadastro formatado na tela com indice
    """
    cadastro = cadastro_jogadores[indice]
    gols = cadastro['gols']
    print(f"O jogador {cadastro['nome']} jogou {cadastro['partidas']} partidas")
    for c, valor in enumerate(gols, start=1):
        print(f"  Na partida {c}, fez {valor} gols")

    print(f"Marcou no campeonato : {cadastro['total']} gols")
    print("-="*30)


def le_int(mensagem):
    """
    le numero digitado pelo usuario
    Repete ate que seja valido

    Retorna:
        valor(int) - número inteiro digitado
    """
    while True:
        try:
            valor = int(input(mensagem))
            break
        except ValueError:
            print("Valor digitado inválido, digite novamente.")
    return valor


#Programa principal
jogadores = multi_cadastro_jogadores()
if jogadores:
    imprime_cadastro(jogadores)
    while True:
        indice = le_int('Mostrar dados de qual jogador(999 encerra): ')
        if indice == 999:
            break
        elif indice < len(jogadores):
            imprime_gols(jogadores,indice)
        else:
            print("valor digitado invalido")
        
print(">>>ENCERRADO<<<")