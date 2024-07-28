
class estruturasLogicas:
    def atividade001():
        numero : int = int(input("Digite um número: "))
        if numero < 0:
            print("Número negativo")
        elif numero > 0:
            print("Número positivo")
        elif numero == 0:
            print("Número zero")

    def atividade002():
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
        temperatura = float(input("Qual é a previsão do tempo para amanhã? Temperatura: "))
        chuva = input("Vai chover?(sim/não): ")

        if temperatura > 20:
            print("Use jeans e camiseta")
        elif temperatura > 10:
            print("Use jeans e camiseta")
            print("Recomendo um suéter também")
        elif temperatura > 5:
            print("Use jeans e camiseta")
            print("Recomendo um casaco")

        if chuva.lower() == 'sim':
            print("Recomendo um guarda-chuva")

    def atividade25():
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")

    def atividade26():
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

    def atividade27():
        preco = float(input("Digite o preço do produto: "))
        if preco <= 50:
            print("Categoria Econômica")
        elif preco <= 100:
            print("Categoria Intermediária")
        else:
            print("Categoria Premium")

    def atividade28():
        idade  = int(input("Digite a sua idade: "))
        if idade >= 16:
            pint("Pode votar")
        else:
            print("Não pode votar") 

    def atividade29():
        num = int(input("Digite um número: "))
        if num >= 1 and num <= 12: 
            if num == 1:
                print("Janeiro")
            if num == 2:
                print("Fevereiro")
            if num == 3:
                print("Março")
            if num == 4:
                print("Abril")
            if num == 5:
                print("Maio")
            if num == 6:
                print("Junho")
            if num == 7:
                print("Julho")
            if num == 8:
                print("Agosto")
            if num == 9:
                print("Setembro")
            if num == 10:
                print("Outubro")
            if num == 11:
                print("Novembro")
            if num == 12:
                print("Dezembro")
        else:
            print("Mês inválido")

    def atividade30():
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num1 < num2:
            print(f"{num2} é maior que {num1}")
        else:
            print(f"{num1} é igual a {num2}")

    def atividade31():
        name1 = input("Digite o primeiro nome: ")
        idade1 = int(input("Digite a idade do primeiro: "))
        name2 = input("Digite o segundo nome: ")
        idade2 = int(input("Digite a idade do segundo: "))
        
        if idade1 > 60:
            print(f"{name1} é idoso")
        elif idade2 > 60:
            print(f"{name2} é idoso")
        else:
            print("Ambos não são idosos")
            if idade1 > idade2:
                print(f"{name1} é mais velho")
            elif idade1 < idade2:
                print(f"{name2} é mais velho")
            else:
                print("Ambos tem a mesma idade")
    
    def PraticaAndOr():
        num = int(input("Digite um número: "))
        if num >= 5 and num <= 8:
            print("O número está entre 5 e 8")
            
        num2 = int(input("Digite um número: "))
        if num2 < 5 or num2 > 8:
            print("O número não está entre 5 e 8")
            
        num3 = int(input("Digite um número: "))
        if not(num3 >= 5 and num3 <= 8):
            print("O número não está entre 5 e 8")

    def atividade32():
        pass
        
    
    def atividade33():
        idade = int(input("Digite a idade: "))
        if idade < 5:
            print("Suspeito que você não saiba escrever")
        elif idade >= 5 and idade <= 110:
            print(f"Ok, você tem {idade} anos")
        else:
            print("Isso deve ser um erro")
    
    def atividade34():
        name = input("Digite um nome: ")
        if name.lower() == "huguinho" or name.lower() == "zezinho" or name.lower() == "luisinho":
            print("Sobrinho do Pato Donald")
        elif name.lower() == "chiquinho" or name.lower() == "francisquinho":
            print("Sobrinho do Mickey Mouse")
    
    def atividade35():
        pontos = float(input("Digite a quantidade de pontos: "))
        if pontos < 0:
                print("Impossivel")
        elif pontos >= 0 and pontos <= 49:
            print("Falhar")
        elif pontos >= 50 and pontos <= 59:
            print(1)
        elif pontos >= 60 and pontos <= 69:
            print(2)
        elif pontos >= 70 and pontos <= 79:
            print(3)
        elif pontos >= 80 and pontos <= 89:
            print(4)
        elif pontos >= 90 and pontos <= 100:
            print(5)
        else:
            print("Impossivel")
    
    def atividade36():
        num = int(input("Digite um número: "))
        if num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
    
    def atividade37():
        ano = int(input("Digite um ano: "))
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print(f"O ano {ano} é bissexto")
        else:
            print(f"O ano {ano} não é bissexto")
