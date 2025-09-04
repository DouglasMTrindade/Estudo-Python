def area_retangulo():
    """
    Lê valores de largura e comprimento
    Calcula:
        Área - largura*comprimento
    Retorna:
        Area - valor do calculo da área
    """
    print("-="*30)
    largura = le_float('Largura(m):')
    comprimento = le_float('Comprimento(m):')
    print("-="*30)
    area = largura * comprimento

    return largura, comprimento, area


def le_float(mensagem):
    """
    le numero digitado pelo usuario
    Repete ate que seja valido

    Retorna:
        (float) - número digitado valido
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor invalido, digite novamente")




#Programa principal
print("Controle de terreno")
largura, comprimento, area = area_retangulo()

print(f"Terreno: {largura:.2f}m x {comprimento:.2f}m")
print(f"Area total: {area:.2f}m²")

print(">>>ENCERRADO<<<")