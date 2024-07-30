class lista:
    def pratica():
        lista = [1,2,3,4,5]
        while True:
            indice = int(input("Escolha o indice: "))
            novoValor = int(input("Novo valor: "))
            
            if indice < 0 or indice >= len(lista):
                lista.append(novoValor)
            
            if novoValor == '' or indice == '': break
                
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
            if operacao.lower() == 'adição':
                print(f"Lista atual: {lista}")
                item = input("Novo item: ")
                lista.append('')
                lista.append(item)
                print(f"Nova lista: {lista}")
                
            elif operacao.lower() =='remoção':
                print(f"Lista atual: {lista}")
                lista.pop()
                print(f"Nova lista: {lista}")
                
                if lista.count() == 0:
                    print("A lista está vazia.")
            elif operacao == '':
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
                if not valores: break

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
        numeros =[]
        while True:
            entrada_usuario = input("Por favor, digite um número inteiro, deixe em branco sair: ")
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
            print(i, end='*')

    def pratica9():
        num: int = int(input("Digite um número: "))
        for i in range(-num, num + 1):
            if i == 0: continue
            print(i)

    def atividade3():
        pass

    def atividade4():
        
        def lista_estrelas(lista: list[int]):
            for i in lista:
                print(i * '*')
                    
        lista = [3, 1, 1, 8]
        lista_estrelas(lista)
            

    def atividade5():
        
        def anagrama(text1, text2):
            return sorted(text1) == sorted(text2)
    
        print(anagrama("abc","cbaa"))
            



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
        
        lista = [7,9,15,897,2413,6687]
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
        text = 'kdljsdlfkjdlfkjsdlkfjdslf'
        print(text.count('fk'))
        
        newText = 'oi'
        modifiedText = text.replace('oi', 'olá')

    def pratica10():
        def mais_caracteres(text):
            letras = []
            LetraMaisCaracteres = ''
            quantidadeCaracteres = 0
            for i in range(len(text)):
                letras.append(text[i])
            
            for j in range(len(letras)):
                if text.count(letras[j]) > quantidadeCaracteres:
                    LetraMaisCaracteres = letras[j]
                    quantidadeCaracteres = text.count(letras[j])
                
                
            print(f"Letra com mais caracteres: {LetraMaisCaracteres} : {quantidadeCaracteres}")
            
        text = 'lkfjdslaaaaaaf'
        mais_caracteres(text)

    def atividade9():
        pass

    def atividade10():
        pass

    def atividade11():
        pass

    def atividade12():
        pass