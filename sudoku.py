def createSudoku():
    sudoku = []
    for linha in range(9):
        sudoku.append([])
        for coluna in range(9):
            sudoku[linha].append("+")
    return sudoku

def fillSudoku():
    sudoku = createSudoku()
    for linha in sudoku:
        print(linha)

fillSudoku()