from agent import *
from connectFourGame import *

def requestInput() -> int:
    
    # Player move and validation
    playerMove = input("\nChoose a column to play (0-6): ")
    try:
        playerMove = int(playerMove)
    except:
        raise ValueError(f"Input {playerMove} is invalid")
    
    if playerMove < 0 or playerMove > 6:
        raise ValueError(f"{playerMove} is out of range of play")
    
    return playerMove

if __name__ == "__main__":
    game = C4Board()
    game.board = [
        ['x', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'o', 'x', 'o', ' ', ' '],
        ['x', 'x', 'o', 'o', ' ', ' '],
        ['x', 'x', ' ', ' ', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' '],
        ['o', 'o', ' ', ' ', ' ', ' ']
    ]
    agent = AlphaBetaAgent()

    while not boardIsTerminal(game.board): # While game is not in a terminal state
        
        printBoard(game.board)

        # Player's move
        playerMove = requestInput()
        game.playMove(playerMove)
        
        printBoard(game.board)
        input("Continue...")

        # Agent's move
        state = GameState(game.board)
        agentMove = agent.play(state)
        game.playMove(agentMove)
    
    print('a')