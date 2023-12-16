from typing import Self
from copy import deepcopy
from connectFourGame import C4Board, isTerminal

class GameState:

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
    
    def generateSuccessors(self) -> list[Self]:

        nextTurn = 1 if self.turn == 0 else 0
        successors = []
        for row in range(C4Board.length):
            for i in range(C4Board.height):
                if self.board[row][i] == '':
                    
                    newBoard = deepcopy(self.board)
                    newBoard[row][i] = 'x' if self.turn == 0 else 'o'
                    successorState = GameState(newBoard, nextTurn)
                    successors.append(successorState)
                    break
        
        return successors


    
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