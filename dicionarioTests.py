""" meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["banaani"] = "banana"

palavra = input("Por favor, digite uma palavra: ")
if palavra in meu_dicionario:
    print("tradução: ", meu_dicionario[palavra])
else:
    print("Palavra não encontrada") """
    
# +++++++++++++++++++++++++++++++++++++++++++++++

""" lista = {}
lista[5] = [1,2,3]
lista[6] = [4,5,7,5]

for chave, valor in lista:
    print(chave, valor) """

""" meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["banaani"] = "banana"

for chave, valor in meu_dicionario:
    print(chave, valor) """
    
lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]

def contagens(minha_lista):
    palavras = {}
    for palavra in minha_lista:
        if palavra not in palavras:
            palavras[palavra] = 0
        
        palavras[palavra] += 1
    return palavras

print(contagens(lista_palavras))