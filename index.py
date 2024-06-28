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


class operadores:
    
    def teste():
        print("Iniciando função teste")
        ano = int(input("Digite um ano:"))
        print(f"Ao fim de 2024 voocê terá {2024 - ano}")


    def atividade6():
        print("Iniciando função atividade 6")
        num = int(input("Digite um número:"))
        print(f"O número é {num} e ele multiplicado por 5 é {num * 5}")


    def atividade7():
        print("Iniciando função atividade 7")
        name = input("Digite seu nome:")
        year = int(input("Digite seu ano de nascimento:"))
        
        print(f"Nome: {name}\nIdade: {year} anos\nOlá {name}, você terá {2024 - year} anos no final do ano de 2024")


    def atividade8():
        print("Iniciando função atividade 8")
        preco = float(input("Digite o preço do produto:"))
        percentual = float(input("Digite o percentual de desconto:"))
        valorDesconto = preco * (percentual / 100)
        print(f"Preço: {preco}\nPercentual de desconto: {percentual}%\nValor do desconto: {valorDesconto}\nPreço final: {preco - valorDesconto}")


    def atividade9():
        print("Iniciando função atividade 9")
        valorConta = float(input("Digite o valor da conta:"))
        gorjeta = float(input("Digite o percentual da gorjeta:"))
        valorGorjeta = valorConta * (gorjeta / 100)
        print(f"Valor da conta: {valorConta}\nPercentual da gorjeta: {gorjeta}%\nValor da gorjeta: {valorGorjeta}\nValor final da conta com gorjeta: {valorConta + valorGorjeta}")


    def atividade10():
        print("Iniciando função atividade 10")
        valorReais = float(input("Digite um valor:"))
        const_valorDolar = 5.45
        print(f"Valor em reais: {valorReais}\nValor em dólares: {round(valorReais / const_valorDolar, 2)}")


    def atividade11():
        print("Iniciando função atividade 11")
        capitalInicial = float(input("Digite um valor: "))
        taxaJurosAnual = float(input("Digite a taxa de juros anual: "))
        tempo = int(input("Digite o tempo em anos: "))
        jurosSimples = capitalInicial * (taxaJurosAnual / 100) * tempo
        print(f"Juros simples {jurosSimples}")

    def atividade12():
        print("Iniciando função atividade 12")
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        num3 = float(input("Terceiro número: "))
        soma = num1 + num2 + num3
        media = soma / 3
        print(f"Soma: {soma}\nMédia: {media}")


    def atividade13():
        print("Iniciando função atividade 13")
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = largura * altura
        perimetro = 2 * (largura + altura)
        print(f"Área: {area}\nPerímetro: {perimetro}")


    def atividade14():
        print("Iniciando função atividade 14")
        celcius = float(input("Digite a temperatura em celcius: "))
        farenheit = (celcius * 9/5) + 32
        print(f"Temperatura em farenheit: {farenheit}")
        
    def atividade15():
        def atividade3():
            nota1 = float(input("Primeira nota: "))
            nota2 = float(input("Segunda nota: "))
            nota3 = float(input("Terceira nota: "))
            nota4 = float(input("Quarta nota: "))
            media = (nota1 + nota2 + nota3 + nota4) / 4
            print(f"Média: {media}")
        
        def atividade4():
            num = int(input("Digite um número: "))
            if num % 2 == 0:
                print("Par")
            else:
                print("Ímpar")
            # print(f"O número é par? Resposta: {num % 2 == 0}")
                
        def atividade5():
            lista = [12, 10, 7, 5]
            max_value = max(lista)
            print(f"O maior valor da lista é: {max_value}")
            
            """ maior = lista[0]
            for item in lista:
                if item > maior:
                    maior = item
            print(f"O maior valor da lista é: {maior}") """
        
        def atividade11():
            salarioBase = float(input("Salário base: "))
            horasNoMes = float(input("Horas trabalhadas no mês: "))
            salarioHora = salarioBase / horasNoMes
            horasExtras = float(input("horas extras: "))
            percentualHorasExtras = float(input("Percentual de horas extras: "))
            porcentagemHorasExtras = percentualHorasExtras / 100
            valorHoraExtra = salarioHora * porcentagemHorasExtras
            bonus = float(input("Bônus: "))
            salarioBruto = salarioBase + (horasExtras * valorHoraExtra) + bonus
            desconto = float(input("Desconto: "))
            salarioLiquido = salarioBruto - desconto
            print(f"Salário base:{salarioBase}\nHoras trabalhadas no mês: {horasNoMes}\nSalário por hora: {salarioHora}\nHoras extras feitas: {horasExtras}\nPercentual: {porcentagemHorasExtras}\nValor por hora extra: {valorHoraExtra}\nBônus: {bonus}\nSalário bruto: {salarioBruto}\nDesconto: {desconto}\nSalário líquido: {salarioLiquido}")
            
        choice = int(input("Escolha a atividade 3, 4, 5 ou 11: "))
        if choice == 3:
            atividade3()
        elif choice == 4:
            atividade4()
        elif choice == 5:
            atividade5()
        elif choice == 11:
            atividade11()
        else:
            print("Essa atividade não existe")

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

class estruturasLogicas:
    def atividade001():
        numero : int = int(input("Digite um número: "))
        if numero < 0:
            print("Número negativo")
        elif numero > 0:
            print("Número positivo")
        elif numero == 0:
            print("Número zero")

    def atividade001():
        nunm : int = int(input("Digite um número: "))
        if numero == 1984:
            print("Orwell")
            
    def atividade16():
        numero : int = int(input("Digite um número: "))
        if numero < 0:
            print(f"Número {numero} é negativo\nMultiplicado por -1 é: {numero * -1}")
        else:
            print(f"Número {numero}")
            
    def atividade17():
        name = input("Digite o nome: ")
        if name != "Jerry":
            numPorcao = int(input("Digite o número de porções: "))
            precoPorcao = 5.90
            total = numPorcao * precoPorcao
            print(f"Total: {total}")
    
    def atividade18():
        numero = int(input("Digite um número: "))
        if numero < 1000:
            print("Este número é menor que 1000")
            print("Obrigado!!")
            if numero < 100:
                print("Este número é menor que 100")
                print("Obrigado!!")
                if numero < 10:
                    print("Este número é menor que 10")
                    print("Obrigado!!")
        
    
    def atividade19():
        const_name = "Vinicius"
        const_city = "Curitiba"
        const_state = "Paraná"
        const_cep = "12345678"
        
        name = input("Digite seu nome: ")
        if name == const_name:
            print(f"Nome: {const_name}\nCidade: {const_city}\nEstado: {const_state}\nCEP: {const_cep}")
        else:
            print("Esse usuário não existe em nossas bases de daddos")
    
    def atividade20():
        num1 = float(input("Digite o 1º número: "))
        num2 = float(input("Digite o 2º número: "))
        operation = int(input("Escolha 1 para 'Adição', 2 para 'Subtração' ou 3 para 'Multiplicação': "))
        if operation == 1:
            print(f"Resultado: {num1 + num2}")
        elif operation == 2:
            print(f"Resultado: {num1 - num2}")
        elif operation == 3:
            print(f"Resultado: {num1 * num2}")
        else:
            print("Operação inválida")

    def atividade21():
        Fahrenheit = float(input("Digite os graus em Fahrenheit: "))
        Celcius = (Fahrenheit - 32) * (5/9) # ou 1.8
        
        if Celcius < 0:
            print(f"Faz {round(Celcius, 2)}ºC - Brr! está frio aqui!")
        
    def atividade22():
        salarioHora = float(input("Digite o salário por hora: "))
        horasTrabalhadas = float(input("Horas trabalhadas: "))
        diaSemana = input("Digite o dia da semana: ")
        
        if diaSemana != "Domingo":
            salarioDiario = salarioHora * horasTrabalhadas
            print(f"Salario diário: {salarioDiario}")
        else:
            salarioDiario = (salarioHora * 2) * horasTrabalhadas
            print(f"Salario diário: {salarioDiario}")
            
    def atividade23():
        pontos = float(input("Digite quantos pontos: "))
        if pontos > 100:
            bonus = pontos * (10 / 100)
            print(f"Bônus de 10%\n Pontos: {pontos + bonus}")
        else:
            bonus = pontos * (15 / 100)
            print(f"Bônus de 15%\n Pontos: {pontos + bonus}")

    def atividade24():
        pass

    def atividade25():
        pass

    def atividade26():
        pass

    def atividade27():
        pass

    def atividade28():
        pass

    def atividade29():
        pass

    def atividade30():
        pass

    def atividade31():
        pass

    def atividade32():
        pass


""" altura = float(input("Altura: "))
peso =  float(input("peso: "))

imc = peso / (altura ** 2)

print(f"imc: {imc}") """


primeiraEscolha = int(input("Você quer testar as atividades de 'Atividades' ou meus 'testes pessoais'?\nEscolha 1 para 'Atividades' ou 2 para 'testes pessoais': "))

if primeiraEscolha == 1:
    choice = int(input("Escolha uma atividade de 1 a 32: "))
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
    elif choice == 15:
        operadores.atividade15()
    elif choice == 16:
        estruturasLogicas.atividade16()
    elif choice == 17:
        estruturasLogicas.atividade17()
    elif choice == 18:
        estruturasLogicas.atividade18()
    elif choice == 19:
        estruturasLogicas.atividade19()
    elif choice == 20:
        estruturasLogicas.atividade20()
    elif choice == 21:
        estruturasLogicas.atividade21()
    elif choice == 22:
        estruturasLogicas.atividade22()
    elif choice == 23:
        estruturasLogicas.atividade23()
    elif choice == 24:
        estruturasLogicas.atividade24()
    elif choice == 21:
        estruturasLogicas.atividade21()
    elif choice == 25:
        estruturasLogicas.atividade25()
    elif choice == 26:
        estruturasLogicas.atividade26()
    elif choice == 27:
        estruturasLogicas.atividade27()
    elif choice == 28:
        estruturasLogicas.atividade28()
    elif choice == 29:
        estruturasLogicas.atividade29()
    elif choice == 30:
        estruturasLogicas.atividade30()
    elif choice == 31:
        estruturasLogicas.atividade31()
    elif choice == 32:
        estruturasLogicas.atividade32()

elif primeiraEscolha == 2:
    choice = int(input("Escolha um teste de 1 a 4: "))
    if choice == 1:
        testesPessoais.atividade1()
    elif choice == 2:
        testesPessoais.atividade2()
    elif choice == 3:
        testesPessoais.atividade3()
    elif choice == 4:
        testesPessoais.atividade4()