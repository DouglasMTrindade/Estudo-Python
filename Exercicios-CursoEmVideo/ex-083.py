def analisa_parentese (expressao):
    pilha = []
    for simb in expressao:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else :
                pilha.append(')')
                return False
    
    return len(pilha) == 0


entrada = input("Digite a expressão:")


if analisa_parentese(entrada):
    print("Sua expressão esta correta")
else:
    print("Sua expressão esta incorreta")