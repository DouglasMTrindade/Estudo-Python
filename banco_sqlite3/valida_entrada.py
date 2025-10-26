

def le_int(mensagem):
    valido = True
    while valido:
        try:
            valor = int(input(mensagem))
            valido = False
        except ValueError:
            print("Valor digitado invalido, Digite novamente")
    
    return valor