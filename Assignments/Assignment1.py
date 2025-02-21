def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the given player has won the game."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def f(b):
    return all(c != " " for r in b for c in r)


def t():
    b = [[" " for _ in range(3)] for _ in range(3)]
    p = ["X", "O"]
    print("Tic-Tac-Toe Game")
    p(b)
    for t in range(9):
        pl = p[t % 2]
        while 1:
            try:
                r, c = map(int, input(f"P {pl}, row col (0-2): ").split())
                if b[r][c] == " ":
                    b[r][c] = pl
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        p(b)
        if c_w(b, pl):
            print(f"P {pl} wins!")
            return
        if f(b):
            print("Draw!")
            return
    print("Draw!")
