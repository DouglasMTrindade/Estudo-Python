

def le_int(mensagem):
    valido = True
    while valido:
        try:
            valor = int(input(mensagem))
            valido = False
        except ValueError:
            print("Valor digitado invalido, Digite novamente")
    
    return valor


def menu ():
   
    lista_menu = {
        0 : "MENU",
        1 : "Consultar e salvar clima",
        2 : "Lista histórico completo",
        3 : "Filtrar por cidade",
        4 : "Apagar registro",
        5 : "Sair"
    }

    print("MENU")
    for chave,valor in lista_menu.items():
        print(f"[{chave}] - {valor}")

    while True:
        opcao = le_int("Escolha uma opção: ")

        if opcao in lista_menu:
            return opcao
        else:
            print("Opção Inválida! Tente novamente")
            