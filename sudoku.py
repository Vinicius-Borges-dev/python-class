def createSudoku():
    for i in range(3):
            matrizMae.append([])
            for j in range(3):
                matrizMae[i].append([])
                for k in range(3):
                    matrizMae[i][j].append([])
                    for l in range(3):
                        matrizMae[i][j][k].append(0)

fillSudoku()