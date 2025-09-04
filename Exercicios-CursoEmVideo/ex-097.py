def escreva(mensagem):
    """
    Imprime mensagem formatada pelo tamanho da string
    Recebe:
        mensagem - string com mensagem
    Retorna:
        None - imprime mensagem formatada na tela
    """
    tamanho = len(mensagem) + 2
    print("-"*tamanho)
    print(f" {mensagem} ")
    print("-"*tamanho, end ="\n\n")



#programa principal
print("Escreva o texto(Enter para encerrar)")
while True:
    mensagem = input("Texto: ")
    if mensagem == '':
        break
    escreva(mensagem)

print(">>>Encerrado<<<")
