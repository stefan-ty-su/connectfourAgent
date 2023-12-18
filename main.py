from agent import *
from connectFourGame import *
import sys, getopt

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

def main(argv) -> None:

    opts, args = getopt.getopt(argv, "a:")
    if len(opts) < 1:
        raise Exception("Not enough arguments")
    for opt, arg in opts:
        if opt == '-a':
            if arg.lower() == "minimax":
                print("Using Mini-Max agent")
                agent = MiniMaxAgent()
            elif arg.lower() == "alphabeta":
                print("Using Alpha-Beta agent with Iterative Deepening")
                agent = AlphaBetaAgent()

    game = C4Board()

    while not boardIsTerminal(game.board): # While game is not in a terminal state
        
        printBoard(game.board)

        # Player's move
        playerMove = requestInput()
        game.playMove(playerMove)
        
        printBoard(game.board)
        input("Continue...")

        # Agent's move
        state = GameState(game.board, game.turn)
        agentMove = agent.play(state)
        game.playMove(agentMove)
    
    winner = state.isWin()
    if winner != ' ':
        print(f"The winner is {winner}")
    else:
        print("There is no winner")

if __name__ == "__main__":
    main(sys.argv[1:])