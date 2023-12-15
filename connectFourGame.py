
class C4Board:

    def __init__(self) -> None:
        
        self.height = 6 # Col -> Transposed Row
        self.length = 7 # Row -> Transposed Col
        self.board = [['' for i in range(self.height)] for j in range(self.length)]
        self.turn = 0

    def playMove(self, row: int) -> None:

        if row >= self.length or row < 0:
            raise ValueError(f'Row Value: {row} is invalid')

        # Assigning char for player ('x' always goes first)
        if self.turn == 0:
            player = 'x'
            self.turn = 1
        else:
            player = 'o'
            self.turn = 0

        for j in range(self.height): # Iterating for through each value in row
            num = self.board[row][j]
            if num == '':
                self.board[row][j] = player
                break
        else: # If loop runs and break does not occur, then play is invalid
            raise ValueError(f'Row {row} is full')
    
    def getValidMoves(self) -> list[int]:

        validMoves = []
        for row in range(self.length):
            for i in range(self.height-1, -1, -1):
                if self.board[row][i] == '':
                    validMoves.append(row)
                    break
        
        return validMoves
    
    def isTerminal(self) -> bool:

        # Checking Rows
        for row in self.board:
            for j in range(self.height-3):
                if row[j] != '' and row[j] == row[j+1] == row[j+2] == row[j+3]:
                    print('A')
                    return True
        
        # Checking Cols
        for j in range(self.height):
            for i in range(self.length-3):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                    return True
        
        # Checking Descending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-3):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    return True
        
        # Checking Ascending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-1, 3, -1):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                    return True
        
        filled = True
        for i in range(self.length):
            if self.board[i][self.height-1] == '':
                filled = False

        return filled

    def getTurn(self):
        return self.turn



board = C4Board()
board.board = [
    ['x', 'o', 'x', 'o', 'x', 'o'],
    ['', '', '', 'o', '', ''],
    ['', '', '', 'o', '', ''],
    ['', '', 'o', 'o', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
]
print(board.isTerminal())

        
