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


    def atividade1():
        num = int(input("Digite um número:"))
        print(f"O número é {num} e ele multiplicado por 5 é {num * 5}")


    def atividade2():
        name = input("Digite seu nome:")
        year = int(input("Digite seu ano de nascimento:"))
        
        print(f"Nome: {name}\nIdade: {year} anos\nOlá {name}, você terá {2024 - year} anos no final do ano de 2024")


    def atividade3():
        s


    def atividade4():
        s


    def atividade5():
        s


    def atividade6():
        s


    def atividade7():
        s


    def atividade8():
        s


    def atividade9():
        s


    def atividade10():
        s


tipo = input("Escolha entre variaveis e operadores:")

if tipo == "variaveis":
    choice = int(input("Escolha uma atividade de 1 a 5:"))
    
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
    else:
        print("Escolha inválida. Por favor, escolha um número de 1 a 15.")
elif tipo == "operadores":
    
    choice = int(input("Escolha uma atividade de 1 a 5:"))
    
    if choice == 1:
        operadores.atividade1()
    elif choice == 2:
        operadores.atividade2()
    elif choice == 3:
        operadores.atividade3()
    elif choice == 4:
        operadores.atividade4()
    elif choice == 5:
        operadores.atividade5()
    elif choice == 6:
        operadores.atividade6()
    elif choice == 7:
        operadores.atividade7()
    elif choice == 8:
        operadores.atividade8()
    elif choice == 9:
        operadores.atividade9()
    else:
        print("Escolha inválida. Por favor, escolha um número de 1 a 15.")