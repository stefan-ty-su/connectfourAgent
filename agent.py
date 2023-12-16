from typing import Self
from copy import deepcopy
from connectFourGame import C4Board, isTerminal

class GameState:

    evaluationBoard = [
        [3, 4, 5, 5, 4, 3],
        [4, 6, 8, 8, 6, 4],
        [5, 8, 11, 11, 8, 5],
        [7, 10, 13, 13, 10, 7],
        [5, 8, 11, 11, 8, 5],
        [4, 6, 8, 8, 6, 4],
        [3, 4, 5, 5, 4, 3]
    ]

    def __init__(self, board: C4Board = None, turn: int = 0) -> None:
        
        self.height = C4Board.height
        self.length = C4Board.length
        if board is None:
            self.board = [['' for i in range(self.height)] for j in range(self.length)]
        else:
            self.board = board
        self.turn = turn

    def isTerminal(self) -> bool:
        return isTerminal(self.board)
    
    def isWin(self) -> str:
        winner = ''
        # Checking Rows
        for row in self.board:
            for j in range(self.height-3):
                if row[j] != '' and row[j] == row[j+1] == row[j+2] == row[j+3]:
                    winner = row[j]
        
        # Checking Cols
        for j in range(self.height):
            for i in range(self.length-3):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                    winner = self.board[i][j]
        
        # Checking Descending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-3):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    winner = self.board[i][j]
                    
        # Checking Ascending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-1, 3, -1):
                if self.board[i][j] != '' and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                    winner = self.board[i][j]

        return winner

    def generateSuccessors(self) -> list[Self]:

        nextTurn = 1 if self.turn == 0 else 0
        successors = []
        for row in range(self.length):
            for i in range(self.height):
                if self.board[row][i] == '':
                    
                    newBoard = deepcopy(self.board)
                    newBoard[row][i] = 'x' if self.turn == 0 else 'o'
                    successorState = GameState(newBoard, nextTurn)
                    successors.append(successorState)
                    break
        
        return successors

    def evaluate(self) -> float:
    
        utility = 138 # Derived from half of total sum of eval table
        if self.turn == 0: # Player = 'x'
            multipler = 1
        else:
            multipler = -1
        
        winner = self.isWin() # If there is a winner, return highest possible u-score
        if winner == 'x':
            return multipler * 500
        elif winner == 'o':
            return multipler * -500
        
        for i in range(self.length):
            for j in range(self.height):
                if self.board[i][j] == 'x':
                    utility += multipler * GameState.evaluationBoard[i][j]
                elif self.board[i][j] == 'o':
                    utility -= multipler * GameState.evaluationBoard[i][j]

        return utility
    
if __name__=="__main__":
    b = [
        ['x', 'o', 'x', 'o', 'x', 'o'],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', '']
    ]
    state = GameState(b)
    successors = state.generateSuccessors()
    for i, successor in enumerate(successors):

        print(f'{i}: {successor.board}, {successor.turn}')