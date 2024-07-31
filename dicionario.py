class dicionario:
    def pratica1():
        
        def histogram(text):
            dicionario = {}
            for item in text:
                
                if item not in dicionario:
                    dicionario[item] = 0
                
                dicionario[item] += 1
            
            for i in dicionario:
                print(f"{i} {dicionario[i] * "*"}")
        

        histogram("Abublé")
        
    def atividade11():
        
        dicionario = {}
        
        def buscar(search):
            if search in dicionario:
                print(dicionario[search])
        
        def adicionar():
            nome = input("Nome: ")
            telefone = input("número: ")
            dicionario[nome] = telefone
        
        
        while True:
            comando = int(input("1 - busca\n2 - adiciona\n3 - sai\n: "))
        
            if comando == 1:
                nome = input("Nome: ")
                buscar(nome)
            elif comando == 2:
                adicionar()
            elif comando == 3:
                print("saindo...")
                break
                
        
        
        
dicionario.atividade11()
