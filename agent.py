from typing import Self
from copy import deepcopy
from connectFourGame import C4Board, boardIsTerminal
from math import inf
import time

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
            self.board = [[' ' for i in range(self.height)] for j in range(self.length)]
        else:
            self.board = board
        self.turn = turn

    def isTerminal(self) -> bool:
        # Checking Rows
        for row in self.board:
            for j in range(self.height-3):
                if row[j] != ' ' and row[j] == row[j+1] == row[j+2] == row[j+3]:
                    return True
        
        # Checking Cols
        for j in range(self.height):
            for i in range(self.length-3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                    return True
        
        # Checking Descending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    return True
        
        # Checking Ascending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-1, 2, -1):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                    return True
        
        filled = True
        for i in range(self.length):
            if self.board[i][self.height-1] == ' ':
                filled = False

        return filled
    
    def isWin(self) -> str:
        winner = ' '
        # Checking Rows
        for row in self.board:
            for j in range(self.height-3):
                if row[j] != ' ' and row[j] == row[j+1] == row[j+2] == row[j+3]:
                    winner = row[j]
        
        # Checking Cols
        for j in range(self.height):
            for i in range(self.length-3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                    winner = self.board[i][j]
        
        # Checking Descending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-3):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    winner = self.board[i][j]
                    
        # Checking Ascending Diagonals
        for i in range(self.length-3):
            for j in range(self.height-1, 2, -1):
                if self.board[i][j] != ' ' and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                    winner = self.board[i][j]

        return winner

    def generateSuccessors(self) -> list[Self]:

        nextTurn = 1 if self.turn == 0 else 0
        successors = []
        for row in range(self.length):
            for i in range(self.height):
                if self.board[row][i] == ' ':
                    
                    newBoard = deepcopy(self.board)
                    newBoard[row][i] = 'x' if self.turn == 0 else 'o'
                    successorState = GameState(newBoard, nextTurn)
                    successors.append(successorState)
                    break
        
        return successors

    def generateActions(self) -> list[int]:

        actions = []
        for i in range(self.length):
            for j in range(self.height):
                if self.board[i][j] == ' ':
                    actions.append(i)
                    break
        
        return actions

    def generateSuccessor(self, action: int) -> Self:
        
        nextTurn = 1 if self.turn == 0 else 0
        newBoard = deepcopy(self.board)
        for i, value in enumerate(newBoard[action]):
            if value == ' ':
                newBoard[action][i] = 'x' if self.turn == 0 else 'o'
                break
        
        return GameState(newBoard, nextTurn)

    def evaluate(self, player: str) -> float:
    
        utility = 138 # Derived from half of total sum of eval table
        if player == 'x': # Player = 'x'
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

class MiniMaxAgent:

    depthLimit = 5
    def __init__(self) -> None:
        pass

    def play(self, gameState: GameState) -> int:
        st = time.time()
        # Determining who the agent is
        if gameState.turn == 0:
            player = 'x'
        else:
            player = 'o'

        actions = gameState.generateActions()
        maxVal = -inf
        maxAction = None
        depth = 0
        for action in actions:
            successor = gameState.generateSuccessor(action)
            value = self.minValue(successor, player, depth)
            print(f'{action}: {value}')
            if value > maxVal:
                maxVal = value
                maxAction = action

        print(f"Calculation Time: {round(time.time() - st,3)}s")
        return maxAction
    
    def minValue(self, gameState: GameState, player: str, depth) -> int:
        if gameState.isTerminal() or depth > MiniMaxAgent.depthLimit: 
            return gameState.evaluate(player)
        depth += 1

        minVal = inf
        actions = gameState.generateActions()
        for action in actions:
            successor = gameState.generateSuccessor(action)
            value = self.maxValue(successor, player, depth)
            if value < minVal:
                minVal = value
        return minVal

    def maxValue(self, gameState: GameState, player: str, depth) -> int:
        if gameState.isTerminal() or depth > MiniMaxAgent.depthLimit: 
            return gameState.evaluate(player)
        depth +=1 

        maxVal = -inf
        actions = gameState.generateActions()
        for action in actions:
            successor = gameState.generateSuccessor(action)
            value = self.minValue(successor, player, depth)
            if value > maxVal:
                maxVal = value
        return maxVal

class AlphaBetaAgent:

    iterDepthLimit = 5
    def __init__(self) -> None:
        pass

    def play(self, gameState: GameState) -> int:
        st = time.time()
        # Determining who the agent is
        if gameState.turn == 0:
            player = 'x'
        else:
            player = 'o'

        alpha = -inf
        beta = inf
        actions = gameState.generateActions()

        for depthLimit in range(1, AlphaBetaAgent.iterDepthLimit+1):
            # print(f'Depth - {depthLimit}')
            maxVal = -inf
            maxAction = None
            for action in actions:
                depth = 0
                successor = gameState.generateSuccessor(action)
                value = self.minValue(successor, alpha, beta, player, depth, depthLimit)
                # print(f'{action}: {value}')
                if value > maxVal:
                    maxVal = value
                    maxAction = action
            if maxVal == 500:
                print(f"Calculation Time: {round(time.time() - st,3)}s")
                return maxAction
        
        print(f"Calculation Time: {round(time.time() - st,3)}s")
        return maxAction
    
    def minValue(self, gameState: GameState, alpha: float, beta: float,  player: str, depth: int, depthLimit: int) -> int:
        if gameState.isTerminal() or depth > depthLimit:
            return gameState.evaluate(player)
        depth += 1

        minVal = inf
        actions = gameState.generateActions()
        for action in actions:
            successor = gameState.generateSuccessor(action)
            minVal = min(minVal, self.maxValue(successor, alpha, beta, player, depth, depthLimit))
            if minVal <= alpha:
                return minVal
            beta = min(beta, minVal)
        return minVal

    def maxValue(self, gameState: GameState, alpha: float, beta: float, player: str, depth: int, depthLimit: int) -> int:
        if gameState.isTerminal() or depth > depthLimit:
            return gameState.evaluate(player)
        depth +=1 

        maxVal = -inf
        actions = gameState.generateActions()
        for action in actions:
            successor = gameState.generateSuccessor(action)
            maxVal = max(maxVal, self.minValue(successor, alpha, beta, player, depth, depthLimit))
            if maxVal >= beta:
                return maxVal
            alpha = max(alpha, maxVal)
        return maxVal

if __name__=="__main__":
    b = [
        ['x', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'o', 'x', 'o', ' ', ' '],
        ['x', 'x', 'o', 'o', ' ', ' '],
        ['x', 'x', 'x', 'o', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' '],
        ['o', 'o', ' ', ' ', ' ', ' ']
    ]
    state = GameState(b)
    state.turn = 1
    # agent = MiniMaxAgent()
    agent = AlphaBetaAgent()
    move = agent.play(state)
    print(move)
    