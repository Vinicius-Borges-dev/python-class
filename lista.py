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
                lista.append(item)
                print(f"Nova lista: {lista}")
            elif operacao.lower() =='remoção':
                print(f"Lista atual: {lista}")
                lista.pop()
                print(f"Nova lista: {lista}")
            elif operacao == '':
                break
                
        
    def atividade1():
        pass

    def atividade2():
        pass

lista.pratica3()