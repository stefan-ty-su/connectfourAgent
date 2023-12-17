
class C4Board:

    height = 6 # Col -> Transposed Row
    length = 7 # Row -> Transposed Col
    def __init__(self) -> None:
        
        self.board = [[' ' for i in range(C4Board.height)] for j in range(C4Board.length)]
        self.turn = 0

    def playMove(self, row: int) -> None:

        if row >= C4Board.length or row < 0:
            raise ValueError(f'Row Value: {row} is invalid')

        print(f'Playing move at column: {row}')
        # Assigning char for player ('x' always goes first)
        if self.turn == 0:
            player = 'x'
            self.turn = 1
        else:
            player = 'o'
            self.turn = 0

        for j in range(C4Board.height): # Iterating for through each value in row
            num = self.board[row][j]
            if num == ' ':
                self.board[row][j] = player
                break
        else: # If loop runs and break does not occur, then play is invalid
            raise ValueError(f'Row {row} is full')

    def getValidMoves(self) -> list[int]:

        validMoves = []
        for row in range(C4Board.length):
            for i in range(C4Board.height-1, -1, -1):
                if self.board[row][i] == ' ':
                    validMoves.append(row)
                    break
        
        return validMoves

    def getTurn(self):
        return self.turn

def boardIsTerminal(board: list[list[str]]) -> bool:

    # Checking Rows
    for row in board:
        for j in range(C4Board.height-3):
            if row[j] != ' ' and row[j] == row[j+1] == row[j+2] == row[j+3]:
                return True
    
    # Checking Cols
    for j in range(C4Board.height):
        for i in range(C4Board.length-3):
            if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                return True
    
    # Checking Descending Diagonals
    for i in range(C4Board.length-3):
        for j in range(C4Board.height-3):
            if board[i][j] != ' ' and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                return True
    
    # Checking Ascending Diagonals
    for i in range(C4Board.length-3):
        for j in range(C4Board.height-1, 3, -1):
            if board[i][j] != ' ' and board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3]:
                return True
    
    filled = True
    for i in range(C4Board.length):
        if board[i][C4Board.height-1] == ' ':
            filled = False

    return filled

def printBoard(board: list[list[str]]) -> bool:

    rotatedBoard = [[board[i][j] for i in range(len(board))] for j in range(len(board[0])-1, -1, -1)]
    print("\n")
    for col in rotatedBoard:
        print(col)


if __name__ == "__main__":
    board = C4Board()
    board.turn = 1
    board.board = [
        ['x', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'o', 'x', 'o', ' ', ' '],
        ['x', 'x', 'o', 'o', ' ', ' '],
        ['x', 'x', 'x', 'o', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' '],
        ['o', 'o', ' ', ' ', ' ', ' ']
    ]
    print(board.evaluate())

        
