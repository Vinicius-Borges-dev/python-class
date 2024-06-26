class variaveis:
    
    def aulaPrint():
        print("Hello world")

    def testeComFor():
        for i in range(0, 10):
            print("Ola mundo vez:", i)

    def aulaMeusDados():
        print("Vinícius")
        print("Moro aqui ó 👉🌍")
        print(21)

    def aulaInputs():
        # Input para escrever o nome
        name = input("Digíte seu nome:")
        print(f"Olá, {name}")
        print("Olá, {}".format(name))

    def aulaPratica():
        nome = "Vinícius"
        idade = 21
        skills = ["frontend development", "backend development", "Design UX/UI"]
        salarioMin = 15000
        SalarioMax = "todos os"
        print(f"Olá, meu nome é {nome}, tenho {idade} anos\nMinhas habilidades são: {skills}\nProcuro um emprego com um salário de {salarioMin} a {SalarioMax} euros por mês")

    def atividade1():
        name = input("Digite seu nome:")
        apelido = input("Digite seu apelido:")
        adress = input("Digite seu endereço:")
        cityAndZip = input("Digite sua cidade e código postal:")
        print(f"Nome próprio: {name}\nApelido: {apelido}\nEndereço: {adress}\nCidade e código postal: {cityAndZip}\n{name} {apelido} {adress} {cityAndZip}")

    # atividade1()

    def atividade2():
        name = input("Digite um nome:")
        year = input("Digite um ano:")
        print(f"{name} é uma valente cavaleira, nascida no ano {year}. Certa manhã, {name} acordou com um barulho terrivel: um dração se aproximava da aldeia. Somente {name} poderia salvar os moradores da aldeia")


    def atividade3():
        city = "São Paulo"
        print(f"Antes: {city}")
        city = "Rio de Janeiro"
        print(f"Depois: {city}")


    def atividade4():
        varStr = "String"
        print(f"Primeira variável: {varStr}")
        varInt = 10
        print(f"Segunda variável: {varInt}")
        varFloat = 10.3
        print(f"Terceira variável: {varFloat}")
        
        print(f"Tipo da primeira: {type(varStr)}\nTipo da segunda: {type(varInt)}\nTipo da terceira: {type(varFloat)}")


    def atividade5():
        first = "Lorem ipsum dolor sit"
        second = "amet, consectetur adipis"
        print(f"{first} {second}")


class operadores:
    
    def teste():
        ano = int(input("Digite um ano:"))
        print(f"Ao fim de 2024 voocê terá {2024 - ano}")


    def atividade6():
        num = int(input("Digite um número:"))
        print(f"O número é {num} e ele multiplicado por 5 é {num * 5}")


    def atividade7():
        name = input("Digite seu nome:")
        year = int(input("Digite seu ano de nascimento:"))
        
        print(f"Nome: {name}\nIdade: {year} anos\nOlá {name}, você terá {2024 - year} anos no final do ano de 2024")


    def atividade8():
        preco = float(input("Digite o preço do produto:"))
        percentual = float(input("Digite o percentual de desconto:"))
        valorDesconto = preco * (percentual / 100)
        print(f"Preço: {preco}\nPercentual de desconto: {percentual}%\nValor do desconto: {valorDesconto}\nPreço final: {preco - valorDesconto}")


    def atividade9():
        valorConta = float(input("Digite o valor da conta:"))
        gorjeta = float(input("Digite o percentual da gorjeta:"))
        valorGorjeta = valorConta * (gorjeta / 100)
        print(f"Valor da conta: {valorConta}\nPercentual da gorjeta: {gorjeta}%\nValor da gorjeta: {valorGorjeta}\nValor final da conta com gorjeta: {valorConta + valorGorjeta}")


    def atividade10():
        valorReais = float(input("Digite um valor:"))
        const_valorDolar = 5.45
        print(f"Valor em reais: {valorReais}\nValor em dólares: {round(valorReais / const_valorDolar, 2)}")


    def atividade11():
        s


    def atividade12():
        s


    def atividade13():
        s


    def atividade14():
        s


class testes:
    def atividade1():
        nome = input("Digite seu nome: ")
        nomeLower = nome.low()
        print(f"Seu nome todo em minúsculo: {nomeLower}")
        nomeUpper = nome.upper()
        print(f"Seu nome todo em maiusculo: {nomeUpper}")

    def atividade2():
        email = input("Digite seu email: ")
        searchChar = input("Digote um caractere que você deseja encontrar no seu email")
        foundChar = email.find(searchChar)
        if foundChar == -1:
            print("Caractere não encontrado")
        else:
            print(f"Caractere encontrado na posição: {foundChar}")

    def atividade3():
        lista = []
        listLen = len(lista)
        print(f"Essa é a lista: {lista} e ela possue tamanho de {listLen}")
        addItem = input("Adicione um item a lista: ")
        lista.append(addItem)
        listLen
        print(f"Agora a sua lista é: {lista} e ela possue um tamanho de {listLen}")

""" altura = float(input("Altura: "))
peso =  float(input("peso: "))

imc = peso / (altura ** 2)

print(f"imc: {imc}") """


primeiraEscolha = int(input("Você quer testar as atividades ou meus testes pessoais\nEscolha 1 para 'atividades' ou 2 para 'testes': "))

if primeiraEscolha == 1:
    choice = int(input("Escolha uma atividade de 1 a 14: "))
    if choice == 1:
        variaveis.atividade1()
    elif choice == 2:
        variaveis.atividade2()
    elif choice == 3:
        variaveis.atividade3()
    elif choice == 4:
        variaveis.atividade4()
    elif choice == 5:
        variaveis.atividade5()
    elif choice == 6:
        operadores.atividade6()
    elif choice == 7:
        operadores.atividade7()
    elif choice == 8:
        operadores.atividade8()
    elif choice == 9:
        operadores.atividade9()
    elif choice == 10:
        operadores.atividade10()
    elif choice == 11:
        operadores.atividade11()
    elif choice == 12:
        operadores.atividade12()
    elif choice == 13:
        operadores.atividade13()
    elif choice == 14:
        operadores.atividade14()
        
elif primeiraEscolha == 2:
    choice = int(input("Escolha um teste de 1 a 3: "))
    if choice == 1:
        testes.atividade1()
    elif choice == 2:
        testes.atividade2()
    elif choice == 3:
        testes.atividade3()