'''
This Program allows user to play Tic Tac Toe
'''


gameOver = False
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


##Gets input
def displayBoard():
    for i in range(3):
        print()
        print("_____________")
        for j in range(3):
            print(board[i][j] + " | ", end = " ")
    print()
def checkRow(row):
   while not 0 <= row <= 2:
       print("Row not valid")
       row = int(input("Enter the row (1-3) where you would like to place your value ")) - 1
   return row

def checkColumn(column):
    while not 0 <= column <= 2:
        print("column not valid")
        column = int(input("Enter the column (1-3) where you would like to place your value ")) -1
    return column
def checkSpot(row, column):
    while board[row][column] != " ":
        print("Spot is taken")
        row = int(input("Enter the row (1-3) where you would like to place your value ")) - 1
        row = checkRow(row)
        column = int(input("Enter the column (1-3) where you would like to place your value ")) -1
        column = checkColumn(column)
    return row, column

def isWinner():
    ## checks row for win
    for i in range(3):
        if (board[i][0] != ' ') and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            return True
    ## checks column for win
    for j in range(3):
        if (board[0][j] != ' ') and (board[0][j] == board[1][j]) and (board[1][j] == board[2][j]):
            return True
    ## checks diagonal for win
    if (board[0][0] != " ") and (board[0][0] == board [1][1]) and (board[1][1] == board [2][2]):
        return True
    if (board[0][2] != " ") and (board[0][2] == board [1][1]) and (board[1][1] == board [2][0]):
        return True
    return False

def isCat():
    filledRow = 0
    for i in range(3):
        if ' ' not in board[i]:
            filledRow +=1
    if filledRow == 3 and isWinner() == False:
        return True
    return False









## gets inputs and checks if they are valid
def getInput():
    global gameOver
    while gameOver == False:
        for i in range(2):
            if i == 0:
                displayBoard()
                row = int(input("Player X, Enter the row (1-3) where you would like to place X ")) -1
                row = checkRow(row)
                column = int(input("Player X, Enter the column (1-3) where you would like to place X ")) -1
                column = checkColumn(column)
                row, column = checkSpot(row, column)
                board[row][column] = "X"
                displayBoard()
                if isWinner() == True:
                    print("Player X won")
                    gameOver = True
                    break
                if isCat() == True:
                    print("It is a tie")
                    gameOver = True
                    break
            else:
                row = int(input("Player O, Enter the row (1-3) where you would like to place O ")) -1
                row = checkRow(row)
                column = int(input("Player O, Enter the column (1-3) where you would like to place O ")) -1
                column = checkColumn(column)
                row, column = checkSpot(row, column)
                board[row][column] = "O"
                displayBoard()
                if isWinner() == True:
                    print("Player O won")
                    gameOver = True
                    break
                if isCat() == True:
                    print("It is a tie")
                    gameOver = True
                    break
getInput()
