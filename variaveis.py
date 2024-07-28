class variaveis:
    
    def aulaPrint():
        print("Iniciando função aulaPrint")
        print("Hello world")

    def testeComFor():
        print("Iniciando função testeComFor")
        for i in range(0, 10):
            print("Ola mundo vez:", i)

    def aulaMeusDados():
        print("Iniciando função aulaMeusDados")
        print("Vinícius")
        print("Moro aqui ó 👉🌍")
        print(21)

    def aulaInputs():
        print("Iniciando função aulaInputs")
        # Input para escrever o nome
        name = input("Digíte seu nome:")
        print(f"Olá, {name}")
        print("Olá, {}".format(name))

    def aulaPratica():
        print("Iniciando função aulaPratica")
        nome = "Vinícius"
        idade = 21
        skills = ["frontend development", "backend development", "Design UX/UI"]
        salarioMin = 15000
        SalarioMax = "todos os"
        print(f"Olá, meu nome é {nome}, tenho {idade} anos\nMinhas habilidades são: {skills}\nProcuro um emprego com um salário de {salarioMin} a {SalarioMax} euros por mês")

    def atividade1():
        print("Iniciando função atividade 1")
        name = input("Digite seu nome:")
        apelido = input("Digite seu apelido:")
        adress = input("Digite seu endereço:")
        cityAndZip = input("Digite sua cidade e código postal:")
        print(f"Nome próprio: {name}\nApelido: {apelido}\nEndereço: {adress}\nCidade e código postal: {cityAndZip}\n{name} {apelido} {adress} {cityAndZip}")

    # atividade1()

    def atividade2():
        print("Iniciando função atividade 2")
        name = input("Digite um nome:")
        year = input("Digite um ano:")
        print(f"{name} é uma valente cavaleira, nascida no ano {year}. Certa manhã, {name} acordou com um barulho terrivel: um dração se aproximava da aldeia. Somente {name} poderia salvar os moradores da aldeia")


    def atividade3():
        print("Iniciando função atividade 3")
        city = "São Paulo"
        print(f"Antes: {city}")
        city = "Rio de Janeiro"
        print(f"Depois: {city}")


    def atividade4():
        print("Iniciando função atividade 4")
        varStr = "String"
        print(f"Primeira variável: {varStr}")
        varInt = 10
        print(f"Segunda variável: {varInt}")
        varFloat = 10.3
        print(f"Terceira variável: {varFloat}")
        
        print(f"Tipo da primeira: {type(varStr)}\nTipo da segunda: {type(varInt)}\nTipo da terceira: {type(varFloat)}")


    def atividade5():
        print("Iniciando função atividade 5")
        first = "Lorem ipsum dolor sit"
        second = "amet, consectetur adipis"
        print(f"{first} {second}")
