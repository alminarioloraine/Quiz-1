# Console-Based Tic Tac Toe

board = [" " for _ in range(9)]
current_player = "X"

def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner():
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if (board[condition[0]] ==
            board[condition[1]] ==
            board[condition[2]] != " "):
            return True
    return False

def check_draw():
    return " " not in board

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Main Game Loop
while True:
    print_board()
    print(f"Player {current_player}'s turn")

    try:
        move = int(input("Enter position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position! Choose 1-9.")
            continue

        if board[move] != " ":
            print("Spot already taken!")
            continue

        board[move] = current_player

        if check_winner():
            print_board()
            print(f"🎉 Player {current_player} wins!")
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        switch_player()

    except ValueError:
        print("Please enter a number between 1-9.")
