from variaveis import variaveis
from operadores import operadores
from estruturasLogicas import estruturasLogicas
from loops import loops
from estrutura import estrutura
from lista import lista

firstChoice = int(input("1 - variaveis\n2 - operadores\n3 - estruturas lógicas\n4 - loops\n5 - estrutura\n6 - lista\nEscolha uma opção: "))

match firstChoice:
    case 1:
        choice = int(input("Escolha atividades de 1 a 5: "))
        match choice:
            case 1:
                variaveis.atividade1()
            case 2:
                variaveis.atividade2()
            case 3:
                variaveis.atividade3()
            case 4:
                variaveis.atividade4()
            case 5:
                variaveis.atividade5()
    case 2:
        choice = int(input("Escolha atividades de 6 a 11: "))
        match choice:
            case 6:
                operadores.atividade6()
            case 7:
                operadores.atividade7()
            case 8:
                operadores.atividade8()
            case 9:
                operadores.atividade9()
            case 10:
                operadores.atividade10()
            case 11:
                operadores.atividade11()
    case 3:
        choice = int(input("Escolha atividades de 16 a 37: "))
        match choice:
            case 16:
                estruturasLogicas.atividade16()
            case 17:
                estruturasLogicas.atividade17()
            case 18:
                estruturasLogicas.atividade18()
            case 19:
                estruturasLogicas.atividade19()
            case 20:
                estruturasLogicas.atividade20()
            case 21:
                estruturasLogicas.atividade21()
            case 22:
                estruturasLogicas.atividade22()
            case 23:
                estruturasLogicas.atividade23()
            case 24:
                estruturasLogicas.atividade24()
            case 25:
                estruturasLogicas.atividade25()
            case 26:
                estruturasLogicas.atividade26()
            case 27:
                estruturasLogicas.atividade27()
            case 28:
                estruturasLogicas.atividade28()
            case 29:
                estruturasLogicas.atividade29()
            case 30:
                estruturasLogicas.atividade30()
            case 31:
                estruturasLogicas.atividade31()
            case 32:
                estruturasLogicas.atividade32()
            case 33:
                estruturasLogicas.atividade33()
            case 34:
                estruturasLogicas.atividade34()
            case 35:
                estruturasLogicas.atividade35()
            case 36:
                estruturasLogicas.atividade36()
            case 37:
                estruturasLogicas.atividade37()
    case 4:
        choice = int(input("Escolha atividades de 38 a 58: "))
        match choice:
            case 38:
                loops.atividade38()
            case 39:
                loops.atividade39()
            case 40:
                loops.atividade40()
            case 41:
                loops.atividade41()
            case 42:
                loops.atividade42()
            case 43:
                loops.atividade43()
            case 44:
                loops.atividade44()
            case 45:
                loops.atividade45()
            case 46:
                loops.atividade46()
            case 47:
                loops.atividade47()
            case 48:
                loops.atividade48()
            case 49:
                loops.atividade49()
            case 50:
                loops.atividade50()
            case 51:
                loops.atividade51()
            case 52:
                loops.atividade52()
            case 53:
                loops.atividade53()
            case 54:
                loops.atividade54()
            case 55:
                loops.atividade55()
            case 56:
                loops.atividade56()
            case 57:
                loops.atividade57()
            case 58:
                loops.atividade58()
    case 5:
        choice = int(input("Escolha atividades de 1 a 10: "))
        match choice:
            case 1:
                estrutura.atividade1()
            case 2:
                estrutura.atividade2()
            case 3:
                estrutura.atividade3()
            case 4:
                estrutura.atividade4()
            case 5:
                estrutura.atividade5()
            case 6:
                estrutura.atividade6()
            case 7:
                estrutura.atividade7()
            case 8:
                estrutura.atividade8()
            case 9:
                estrutura.atividade9()
            case 10:
                estrutura.atividade10()
    case 6:
        choice = int(input("Escolha atividades de 1 a 11: "))
        match choice:
            case 1:
                lista.xadrez()
            