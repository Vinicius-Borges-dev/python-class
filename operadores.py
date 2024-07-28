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
