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
            
            
    def atividade1():
        pass

    def atividade2():
        pass

lista.pratica4()