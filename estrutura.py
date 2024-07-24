def pratica():
        nomes = [];
        while len(nomes) != 7:
            nome = input("Digite o nome de algum irmão: ")
            nomes.append(nome)
            
        print(sorted(nomes))

def atividade1():
    notas = [];
    while len(notas) <= 2:
        nota = int(input("Digite a nota do aluno: "))
        notas.append(nota)

    def media(notas):
        media = sum(notas) / len(notas)
        print(f"Média: {media}")
        
    media(notas)

# Atividade 2
def printa_varias_vezes(text, vezes):
    print(text*vezes)

def atividade2():
    tamanho = int(input("Digite o tamanho do quadrado: "))
    def quadrado_hashtag(tamanho):
        count = 1
        while True:
            print('#' * tamanho)
            if count == tamanho: break
            count += 1
            
    quadrado_hashtag(tamanho)

def atividade3():
    tamanho = int(input("Digite o tamanho do quadrado: "))
    def mesaXadrez(tamanho):
        x = 0
        while x < tamanho:
            y = 0
            while y < tamanho:
                if (x + y) % 2 == 0:
                    print("1", end="")
                else:
                    print("0", end="")
                y += 1
            print()
            x += 1
            
    mesaXadrez(tamanho)

atividade3()