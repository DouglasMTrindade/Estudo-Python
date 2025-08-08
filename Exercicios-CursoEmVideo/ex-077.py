palavras = ("curso", "python", "banana")

for palavra in palavras:
    vogais = [letra for letra in palavra if letra.lower() in "aeiou"]
    print (f"A palavra {palavra.upper()} tem as vogais: {", ".join(vogais)}")
