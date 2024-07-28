
class testesPessoais:
    def atividade1():
        print("Iniciando função atividade 1")
        nome = input("Digite seu nome: ")
        nomeLower = nome.lower()
        print(f"Seu nome todo em minúsculo: {nomeLower}")
        nomeUpper = nome.upper()
        print(f"Seu nome todo em maiusculo: {nomeUpper}")


    def atividade2():
        print("Iniciando função atividade 2")
        email = input("Digite seu email: ")
        searchChar = input("Digite um caractere que você deseja encontrar no seu email: ")
        foundChar = email.find(searchChar)
        if foundChar == -1:
            print("Caractere não encontrado")
        else:
            print(f"Caractere encontrado na posição: {foundChar}")


    def atividade3():
        print("Iniciando função atividade 3")
        lista = []
        listLen = len(lista)
        print(f"Essa é a lista: {lista} e ela possue tamanho de {listLen}")
        addItem = input("Adicione um item a lista: ")
        lista.append(addItem)
        listLen = len(lista)
        print(f"Agora a sua lista é: {lista} e ela possue um tamanho de {listLen}")


    def atividade4():
        print("Iniciando função atividade 4")
        lista = ["item1", "item2", "item3"]
        print(f"Essa é a lista: {lista}")
        removeItem = input("Digite o item que você deseja remover: ")
        lista.remove(removeItem)
        print(f"Agora a sua lista é: {lista}")


    def atividade5():
        s
