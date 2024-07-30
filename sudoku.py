def criarSudoku():
    sudoku = []
    for linha in range(9):
        sudoku.append([])
        for coluna in range(9):
            sudoku[linha].append("+")
    return sudoku

    for linha in criarSudoku():
        print(linha)

print(criarSudoku())