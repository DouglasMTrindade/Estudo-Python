def cadastro_jogador():
    """
    Cadastro de jogador nome e dados das partidas jogadas

    Retorna:
        cadastro(dict):{nome, partidas, gols, total}
    """
    cadastro ={}
    cadastro['nome'] = input("Nome: ").strip().capitalize()

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


def imprime_cadastro(cadastro):
    """
    Imprime o cadastro do jogador realizado
    Recebe:
        Cadastro(dict) - com dados do jogador cadastrado
    Retorna:
        None - imprime cadastro formatado na tela
    """
    print("-="*30)
    for chave, valor in cadastro.items():
        print(f"{chave.capitalize():<12}: {valor}")
    print("-="*30)

    gols = cadastro['gols']
    print(f"O jogador {cadastro['nome']} jogou {cadastro['partidas']} partidas")
    for c, valor in enumerate(gols, start=1):
        print(f"  ==>Na partida {c}, fez {valor} gols")

    print(f"Marcou no campeonato : {cadastro['total']} gols")
    print("-="*30)


def le_int(mensagem):
    """
    le numero digitado pelo usuario
    Repete ate que seja valido

    Retornar:
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
cadastro = cadastro_jogador()
imprime_cadastro(cadastro)