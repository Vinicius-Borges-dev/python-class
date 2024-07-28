class estrutura:
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
    def atividade2():
        
        def printa_varias_vezes(text, vezes):
            print(text*vezes)
            
        text = input("Digite um texto: ")
        vezes = int(input("Digite quantas vezes vai aparecer: "))
        printa_varias_vezes(text, vezes)

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
                    
        text = input("Digite um texto: ")
        tamanhoQuadrado = int(input("Digite o tamanho do quadrado: "))

        quadradoString(text, tamanhoQuadrado)



    def linha(num, text):
        if text == '':
            print('* ' * num)
        else:
            print(text[0] * num)


    def atividade7():

        def caixa_de_hashtag(altura):
            count = 0
            while count < altura:
                estrutura.linha(10, '#')
                count += 1
                
        tamanhoCaixa = int(input("Digite o tamanho da caixa: "))
        caixa_de_hashtag(tamanhoCaixa)

    def atividade8():
        
        def triangulo(tamanho):
            
            rowCount = 0
            colCount = 0
            text= ''
            while rowCount < tamanho:
                while colCount < tamanho:
                    text += '#'
                    print(text)
                    colCount += 1
                rowCount += 1  
                
        tamanhoTriangulo = int(input("Digite o tamamho do triangulo: "))         
        triangulo(tamanhoTriangulo)


    """ Uso de return """
    def atividade9():
        
        def o_maior_numero(lista):
            return max(lista)
            
        count = 1
        lista=[]
        while True:
            numero =int(input(f"Digite o {count}º número: "))
            lista.append(numero)
            count += 1
            if count == 3: break
            
        print(o_maior_numero(lista))
        

    def atividade10():
        
        def mesmo_caracter(text, num1, num2):
            if num1 >= len(text) or num2 >= len(text):
                return False
            elif text[num1] == text[num2]:
                return True
            else:
                return False
            
            
        
        text = input("Digite um texto: ")
        firstIndex = int(input("Digite o indice do primeiro teste: "))
        SecondIndex = int(input("Digite o indice do segundo teste: "))
        print(f"Texto: {text}\nOs caracteres escolhidos são iguais? Resposta: {mesmo_caracter(text, firstIndex, SecondIndex)}")


