class Environment:
    def __init__(self):
        self.board = [' ' for _ in range(9)]


class SimpleTicTacToeAgent:
    def __init__(self, environment):
        self.printBoard(environment)

        while True:
            move = int(input("Enter your position (1-9): ")) - 1

            if move < 0 or move > 8 or environment.board[move] != ' ':
                print("Invalid move!")
                continue

            environment.board[move] = 'X'

            self.printBoard(environment)

            if self.checkWinner(environment, 'X'):
                print("You Win!")
                break

            if self.isFull(environment):
                print("Draw!")
                break

            print("Agent is making a move...")

            if environment.board[4] == ' ':
                environment.board[4] = 'O'
            else:
                for i in range(9):
                    if environment.board[i] == ' ':
                        environment.board[i] = 'O'
                        break

            self.printBoard(environment)

            if self.checkWinner(environment, 'O'):
                print("Agent Wins!")
                break

            if self.isFull(environment):
                print("Draw!")
                break

    def printBoard(self, environment):
        board = environment.board

        print()
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print()

    def checkWinner(self, environment, player):
        winningPositions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winningPositions:
            if environment.board[a] == player and \
               environment.board[b] == player and \
               environment.board[c] == player:
                return True

        return False

    def isFull(self, environment):
        return ' ' not in environment.board


theEnvironment = Environment()
theAgent = SimpleTicTacToeAgent(theEnvironment)
