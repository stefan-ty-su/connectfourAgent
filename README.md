# connectfourAgent
## Description
Implementation of adversarial agent utilising the mini-max algorithm for decision making.
There are two implementations of the mini-max algorithm
- Mini-Max without any algorithmic optimisations (Depth Limit of 5)
- Mini-Max utilising alpha-beta pruning and iterative deepening (Depth Limit of 6)

## Usage
To start a game of connect four, an argument specifying which mini-max implementation to use is required, of which there are two: 'minimax' and 'alphabeta'

### Example
The following example runs a connect 4 game using the mini-max implementation with alpha-beta pruning and iterative deepening
```console
> python main.py -a alphabeta
```
