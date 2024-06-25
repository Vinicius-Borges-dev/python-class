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

aulaPratica()

def atividade1():
    name = input("Digite seu nome:")
    apelido = input("Digite seu apelido:")
    adress = input("Digite seu endereço:")
    cityAndZip = input("Digite sua cidade e código postal:")
    
    print(f"Nome próprio{name}\nApelido: {apelido}\nEndereço: {adress}\nCidade e código postal: {cityAndZip}\n{name} {apelido} {adress} {cityAndZip}")