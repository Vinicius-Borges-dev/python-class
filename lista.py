import random


class lista:
    def pratica():
        lista = [1, 2, 3, 4, 5]
        while True:
            indice = int(input("Escolha o indice: "))
            novoValor = int(input("Novo valor: "))

            if indice < 0 or indice >= len(lista):
                lista.append(novoValor)

            if novoValor == "" or indice == "":
                break

            lista[indice] = novoValor
            print(f"Nova lista: {lista}")

    def pratica2():
        num = int(input("Quantos itens serão adicionados: "))
        lista = []
        while len(lista) != num:
            item = input("Novo item: ")
            lista.append(item)

        print(f"Novo lista: {lista}")

    def pratica3():

        lista = [1]

        while True:
            operacao = input("Escolha entre adição ou remoção de itens: ")
            if operacao.lower() == "adição":
                print(f"Lista atual: {lista}")
                item = input("Novo item: ")
                lista.append("")
                lista.append(item)
                print(f"Nova lista: {lista}")

            elif operacao.lower() == "remoção":
                print(f"Lista atual: {lista}")
                lista.pop()
                print(f"Nova lista: {lista}")

                if lista.count() == 0:
                    print("A lista está vazia.")
            elif operacao == "":
                break

        def classifcacao():
            def teste1():
                minha_lista = [2, 5, 1, 2, 3]
                minha_lista.sort()
                print(minha_lista)

            def teste2():
                original = [2, 6, 1, 2, 4]
                em_ordem = sorted(original)
                print(em_ordem)
                print(original)

        def pratica4():
            lista = []

            while True:
                valores = int(input("Digite um valor: "))
                if not valores:
                    break

                lista.append(valores)
                print(f"Lista normal: {lista}")
                print(f"Lista ordenada: {sorted(lista)}")

    def maxMinSum():
        minha_lista = [2, 5, 1, 2, 2]

        maior = max(minha_lista)
        menor = min(minha_lista)
        soma_lista = sum(minha_lista)

    def pratica5():
        show_tamanhao = [45, 44, 36, 39, 40]

        def mediana(minha_lista: list):
            ordenada = sorted(minha_lista)
            centro_lsta = len(ordenada) // 2
            return ordenada[centro_lsta]

        print(f"A mediana é: {mediana(show_tamanhao)}")

        idades = [1, 56, 34, 27, 5, 77, 5]
        print(f"A mediana das idades: {mediana(idades)}")

    def pratica6():
        numeros = []
        while True:
            entrada_usuario = input(
                "Por favor, digite um número inteiro, deixe em branco sair: "
            )
            if len(entrada_usuario) == 0:
                break
            numeros.append(int(entrada_usuario))
        print(numeros)

    def pratica7():

        def tamanho(lista):
            return len(lista)

        lista = [1, 2, 3, 4, 5]

        tamanho(lista)

    def atividade1():

        def media(lista: list[int]):
            return sum(lista) / len(lista)

    def atividade2():

        def range(lista: list[int]):
            return max(lista) - min(lista)

    def pratica8():
        text = input("Digite um texto: ")
        for i in text:
            print(i, end="*")

    def pratica9():
        num: int = int(input("Digite um número: "))
        for i in range(-num, num + 1):
            if i == 0:
                continue
            print(i)

    def atividade3():
        pass

    def atividade4():

        def lista_estrelas(lista: list[int]):
            for i in lista:
                print(i * "*")

        lista = [3, 1, 1, 8]
        lista_estrelas(lista)

    def atividade5():

        def anagrama(text1, text2):
            return sorted(text1) == sorted(text2)

        print(anagrama("abc", "cbaa"))

    def atividade6():

        def soma_positivo(lista):
            soma = 0
            for i in lista:
                if i > 0:
                    soma += i
            return soma

        lista = [3, 1, -1]

        print(soma_positivo(lista))

    def atividade7():

        def numeros_pares(lista):
            pares = []
            for i in lista:
                if i % 2 == 0:
                    pares.append(i)
            return pares

        lista = [7, 9, 15, 897, 2413, 6687]
        print(f"Números pares: {numeros_pares(lista)}")

    def atividade8():

        def lista_soma(lista1, lista2):
            soma = []
            for i in range(len(lista1)):
                soma.append(lista1[i] + lista2[i])
            return soma

        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]
        print(lista_soma(lista1, lista2))

    def metodoCOunt():
        text = "kdljsdlfkjdlfkjsdlkfjdslf"
        print(text.count("fk"))

        newText = "oi"
        modifiedText = text.replace("oi", "olá")

    def pratica10():
        def mais_caracteres(text):
            letras = []
            LetraMaisCaracteres = ""
            quantidadeCaracteres = 0
            for i in range(len(text)):
                letras.append(text[i])

            for j in range(len(letras)):
                if text.count(letras[j]) > quantidadeCaracteres:
                    LetraMaisCaracteres = letras[j]
                    quantidadeCaracteres = text.count(letras[j])

            print(
                f"Letra com mais caracteres: {LetraMaisCaracteres} : {quantidadeCaracteres}"
            )

        text = "lkfjdslaaaaaaf"
        mais_caracteres(text)

    def atividade9():

        def sem_vogal(text):
            vogais = ["a", "e", "i", "o", "u"]
            for i in text:
                if vogais.count(i) == 0:
                    print(i, end="")

        sem_vogal("banana")

    def listasAninhadas():
        lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(lista[1][2])

        pessoas = [["betty", 20, 1.60], ["John", 35, 1.75]]

        for pessoas in pessoas:
            nome = pessoa[0]
            idade = pessoa[1]
            altura = pessoa[2]

    def sudoku():
        def createSudoku():
            sudoku = []

            linha = 0
            coluna = 0

            while linha <= 6:
                sudoku.append([])
                while coluna <= 6:
                    sudoku[linha].append("+")
                    coluna += 1
                coluna = 0
                linha += 1

            def validaSudoku(sudoku, linha, coluna, numero):
                for item in range(len(sudoku)):
                    if sudoku[linha][item] == numero:
                        return False
                    if sudoku[item][coluna] == numero:
                        return False
                    
                return True

            for linha in range(len(sudoku)):
                for coluna in range(len(sudoku)):
                    while True:
                        
                        RandomNumber = str(random.randint(1, 9))
                        if validaSudoku(sudoku, linha, coluna, RandomNumber) == True:
                            sudoku[linha][coluna] = RandomNumber
                            break

            return sudoku

        sudoku = createSudoku()

        def printSudoku(sudoku):
            linhaExterna = 0
            colunaExterna = 0
            print("    ", end="")
            while linhaExterna <= 8:
                print(linhaExterna, end="    ")
                linhaExterna += 1
            print()

            for linha in sudoku:
                print(f"{colunaExterna} {linha}")
                colunaExterna += 1
                print()

            print()

        printSudoku(sudoku)

        while True:
                
            choiceRow = int(input("Escolha a posição a linha de 0 a 8: "))
            choiceCol = int(input("Escolha a posição a coluna de 0 a 8: "))
            
            if choiceRow == '' or choiceCol == '': break
            if choiceRow < 0 or choiceRow > 8 or choiceCol < 0 or choiceCol > 8:
                print("Posição inválida.")
                continue
            
            newNumber = input("Escolha o número a ser colocado: ")
            
            
            sudoku[choiceCol][choiceRow] = newNumber
            
            printSudoku(sudoku)
            

    def pratica11():

        def conta_elementos_match(lista, elemento):
            quantasVezes = 0
            for linha in lista:
                quantasVezes += linha.count(elemento)

            return quantasVezes

        lista = [[1, 5, 3], [5, 5, 6], [5, 8, 9]]
        elemento = 5
        print(conta_elementos_match(lista, elemento))

    def pratica12():
        sudoku = [
            [9, 0, 0, 0, 8, 0, 3, 0, 0],
            [0, 0, 0, 2, 5, 0, 7, 0, 0],
            [0, 2, 0, 3, 0, 0, 0, 0, 4],
            [0, 9, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 3, 0, 5, 6, 0],
            [7, 0, 5, 0, 6, 0, 4, 0, 0],
            [0, 0, 7, 8, 0, 3, 9, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 2],
        ]
        for linha in sudoku:
            for i in range(len(linha)):
                if linha[i] == 0:
                    print("_", end=" ")
                else:
                    print(linha[i], end=" ")
            print()

    def atividade10():
        def createGridVelha():
            gradeVelha = []

            linha = 0
            coluna = 0

            while linha <= 2:
                gradeVelha.append([])
                while coluna <= 2:
                    gradeVelha[linha].append("+")
                    coluna += 1
                coluna = 0
                linha += 1
            return gradeVelha
        
        def printGridVelha(grid):
            linhaExterna = 0
            colunaExterna = 0
            print("    ", end="")
            while linhaExterna <= 2:
                print(linhaExterna, end="    ")
                linhaExterna += 1
            print()

            for linha in grid:
                print(f"{colunaExterna} {linha}")
                colunaExterna += 1
                print()

            print()
            
        grid = createGridVelha()
        printGridVelha(grid)
        
        winner = ''
        while True:
                
            choiceRow = int(input("Escolha a posição a linha de 0 a 2: "))
            choiceCol = int(input("Escolha a posição a coluna de 0 a 2: "))
            
            if choiceRow == '' or choiceCol == '': break
            if choiceRow < 0 or choiceRow > 2 or choiceCol < 0 or choiceCol > 2:
                print("Posição inválida.")
                break
            
            newSimbol = input("Escolha o simbolo a ser colocado: ")
            
            
            grid[choiceCol][choiceRow] = newSimbol
            
            printGridVelha(grid)
            for linha in grid:
                if linha.count("x") == 3:
                    winner = 'x'
                elif linha.count("o") == 3:
                    winner = 'o'
                else:
                    winner = 'empate'

            acertos = 0
            for i in range(len(grid)):
                if grid[i][choiceRow] == newSimbol:
                    acertos += 1
                
            if acertos == 3:
                print(newSimbol)
                winner = newSimbol
                
            if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
                winner = grid[0][0]
            elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
                winner = grid[0][2]


            if winner == 'x':
                print("Jogador x ganhou")
                break
            elif winner == 'o':
                print("Jogador o ganhou")
                break

    def atividade11():
        pass

    def atividade12():
        pass
