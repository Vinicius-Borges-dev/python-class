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
    print(f"Primera variável: {varStr}")
    varInt = 10
    print(f"Segunda variável: {varInt}")
    varFloat = 10.3
    print(f"Terceira variável: {varFloat}")
    
    print(f"Tipo da primeira: {type(varStr)}, tipo da segunda: {type(varInt)}, tipo da terceira: {type(varFloat)}")


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


def atividade11():
    s


def atividade12():
    s


def atividade13():
    s


def atividade14():
    s


def atividade15():
    s


choice = int(input("Escolha uma atividade: de 1 a 15:"))

if choice == 1:
    atividade1()
elif choice == 2:
    atividade2()
elif choice == 3:
    atividade3()
elif choice == 4:
    atividade4()
elif choice == 5:
    atividade5()
elif choice == 6:
    atividade6()
elif choice == 7:
    atividade7()
elif choice == 8:
    atividade8()
elif choice == 9:
    atividade9()
elif choice == 10:
    atividade10()
elif choice == 11:
    atividade11()
elif choice == 12:
    atividade12()
elif choice == 13:
    atividade13()
elif choice == 14:
    atividade14()
elif choice == 15:
    atividade15()
else:
    print("Escolha inválida. Por favor, escolha um número de 1 a 15.")