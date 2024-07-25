def pratica():
        nomes = [];
        while len(nomes) != 7:
            nome = input("Digite o nome de algum irmão: ")
            nomes.append(nome)
            
        print(sorted(nomes))

def atividade1():
    notas = [];
    while len(notas) <= 2:
        nota = int(input("Digite a nota do aluno: "))
        notas.append(nota)

    def media(notas):
        media = sum(notas) / len(notas)
        print(f"Média: {media}")
        
    media(notas)

# Atividade 2
def printa_varias_vezes(text, vezes):
    print(text*vezes)

def atividade3():
    
    def quadrado_hashtag(tamanho):
        count = 1
        while True:
            print('# ' * tamanho)
            if count == tamanho: break
            count += 1
            
    quadrado_hashtag(4)

def atividade4():
    tamanho = int(input("Digite o tamanho do quadrado: "))
    def mesaXadrez(tamanho):
        x = 0
        while x < tamanho:
            y = 0
            while y < tamanho:
                if (x + y) % 2 == 0:
                    print("1", end="")
                else:
                    print("0", end="")
                y += 1
            print()
            x += 1
            
    mesaXadrez(tamanho)
    

def atividade5():

    def quadradoString(text, num):
        """ lineCounter = 0
        lineContent = ''
        caracterCounter = 0

        while lineCounter < num:
            
            while len(lineContent) < num:
                lineContent += text[caracterCounter]
                if caracterCounter == len(text) - 1:
                    caracterCounter = 0
                else:
                    caracterCounter += 1

            print(lineContent)
            lineContent = lineContent[caracterCounter - (caracterCounter + 1)]
            
            lineContent= lineContent[1:]
            lineCounter += 1 """
            
        lineCounter = 0
        coluna = 0
        linha = 0 
        while linha < num:
            while coluna < num:
                print(text[lineCounter], end='')
                lineCounter += 1
                coluna += 1
                
                if lineCounter == len(text):
                    lineCounter = 0
                    
            print()
            coluna = 0
            linha += 1
                

    quadradoString("Ramalho", 6)

atividade5()



def linha(num, text):
    if text == '':
        print('* ' * num)
    else:
        print(text[0] * num)


def atividade7():

    def caixa_de_hashtag(altura):
        count = 0
        while count < altura:
            linha(10, '')
            count += 1
            
    caixa_de_hashtag(8)
    
""" atividade7() """