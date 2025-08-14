def analisa_parentese (expressao):
    #Verifica os parenteses de uma expressão estao corretos
    pilha = []
    for simb in expressao:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else :
                pilha.append(')')
                return False # ')' sem '(' correspondente
    
    return len(pilha) == 0 #pilha vazia a expressao esta balanceada

#programa principal
entrada = input("Digite a expressão:")

if analisa_parentese(entrada):
    print("Sua expressão esta correta")
else:
    print("Sua expressão esta incorreta")