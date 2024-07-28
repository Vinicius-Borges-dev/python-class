
import re
from math import sqrt
import random

class loops:
    def pratica1():
        while True:
            num = int(input("Digite um número: "))
            if num == -1:
                break
            
            print(num ** 2)
        print("Programa encerrado")

    def pratica2():
        while True:
            codigo = input("Digite um pin: ")
            
            if codigo == '1234':
                break
            
            print("Código inválido")
        print("PIN correto, obrigado")
    
    def atividade38():
        print("Olá")
        while True:
            continuar = input("Deseja continuar? (sim/não): ")
            if continuar.lower() == "não" or continuar.lower() == "n":
                break
            
            
        print("Okay, até a próxima")
    
    def atividade39():
        while True:
            num1 = int(input("Digite um número: "))
            
            if num1 < 0:
                print("Número inválido")
            elif num1 >= 1:
                print(f"Raiz quadrada de {num1}: {sqrt(num1)}")
            else:
                break
        
        print("Fim")
        
    
    
    
    def atividade40():
        numero = 5
        print("Iniciando")
        while True:
            print(numero)
            numero = numero - 1
            if numero == 0:
                break
        
        print("Fim")
        
    
    def atividade41():
        senha = input("Digite a senha: ")
        while True:
            confirma_senha = input("Digite a senha novamente: ")
            if confirma_senha == senha:
                break
            print("Senha incorreta")
        
        print("Senhas são iguais")
        
    def pratica3():
        tentativas = 0
        while True:
            codigo = input("Por favor, digite seu PIN: ")
            tentativas += 1
            if codigo == '1234':
                sucesso = True
                break
            
            if tentativas == 3:
                sucesso = False
                break
            print("Código inválido, digite novamente")
            
        if sucesso:
            print("PIN correto inserido")
        else:
            print("Você excedeu o número de tentativas")
            
    def atividade42():
        tentativas = 0
        while True:
            codigo = input("Por favor, digite seu PIN: ")
            tentativas += 1
            if codigo == '4321':
                sucesso = True
                break
            
        print(f"PIN correto inserido\nNúmero de vezes que tentou: {tentativas}")
        
    
    def atividade43():
        ano = int(input("Digite um ano: "))
        while True:
            ano += 1
            if ano % 4 == 0 and ano % 100 != 0:
                print(f"O próximo ano bissexto é: {ano}")
                break
            
    def pratica4():
        num = int(input("Digite um número: "))
        while num <= 10:
            print(num)
            num += 1
            
    
    def atividade44():
        num = 0
        while num <= 30:
            num += 1
            if num % 2 == 0:
                print(num)

    def atividade45():
        print("Você está pronto?")
        numero = int(input("Por favor, digite um número: "))
        while numero > 0:
            print(numero)
            numero -= 1

        print("Agora!")

    def atividade46():
        num = int(input("Digite um número: "))
        count = 0
        while count <= num:
            print(count)
            count += 1

    def atividade47():
        limitNum = int(input("Digite um número: "))
        count = 1
        while count <= limitNum:
            print(count)
            count *= 2
            
    def pratica5():
        
        print(re.search(r"[A-Z]", "SeNha"))
        
        numero_secreto = random.randint(1, 10)

    def atividade48():
        pass

    def atividade49():
        pass

    def atividade50():
        soma = 0
        while soma != 100:
            numero = int(input("Digite um número: "))
            soma += numero
            print(f"Soma: {soma}")
            if soma == 100:
                break
            elif soma > 100:
                print("Soma maior que 100")
                break

    def atividade51():
        while True:
            senha = input("Digite uma senha: ")
            if len(senha) > 8 or re.search("[A-Z]", senha) != None or re.search("[0-9]", senha) != None:
                break
        
        print("Senha válida")

    def atividade52():
        secret_num = random.randint(1, 100)
        
        while True:
            num = int(input("Digite um número: "))
            
            if num == secret_num:
                print("Você acertou!")
                break
            elif num < secret_num:
                print(f"O número é maior que {num}")
            else:
                print(f"O número é menor que {num}")
                
    def atividade53():
        saldo_diponivel = 4000
        
        while True:
            saque = float(input("Digite o valor do saque: "))
            if saque % 10 == 0 or saque < saldo_disponivel:
                break

        print("Saque válido")

    def pratica6():
        palavra = 'Banana'
        princleart(palavra*3)
        

        
    def atividadePratica():
        firstString = input("Digite alguma coisa: ")
        secondString = input("Digite outra coisa: ")
        
        maior = firstString
        while True:
            if len(maior) < len(secondString):
                maior = secondString
            else:
                break
            
        print(f"Maior string: {maior}")
        
    def comprimentoDoIndice():
        palavra = "Abluble"
        print(palavra[0])
        print(palavra[1])
        print(palavra[3])
        print(f"Último caractere: {palavra[len(palavra) - 1]}") # ou palavra[-1]
        
    def atividadePratica2():
        string = input("Digite alguma coisa: ")
        
        if string[2] == string[-2]:
            print("Segundo e penúltimo caractere são iguais")
            


        #while True:
            #f string[2] == string[-2]:
                #break
        #print("Segundo e penúltimo caractere são iguais")
        
    def atividade55():
        count = int(input("Digite quantas vezes vai aparecer: "))
        print("#" * count)
        
    
    def atividade56():
        while string != "":
            string = input("Digite alguma coisa: ")
            print(string)
            print("-" * len(string))
            
    def atividade57():
        string = input("Digite alguma coisa: ")
        if len(string) < 20:
            count = 20 - len(string)
            string = "*" * count + string

        print(string)

    def atividade58():
        string = input("Digite alguma coisa: ")
        if len(string) < 30:
            count = (30 - len(string)) / 2
            string = ("*" * round(count)) + string + ("*" * round(count))
            if len(string) % 2 != 0 and len(string) < 30:
                string += "*"

        print(f"{"*" * 30}\n{string}\n{"*" * 30}")
        
    def loopAninhamdo():
        while True:
            num: int = int(input("Digite um número: "))
            if num == 1: break
        while numero > 0:
            print(numero)
            numero -= 1
  
