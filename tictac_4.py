import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.YELLOW + cell + Style.RESET_ALL
        return cell

    print(f"{colored(board[0])} | {colored(board[1])} | {colored(board[2])}")
    print("---------")
    print(f"{colored(board[3])} | {colored(board[4])} | {colored(board[5])}")
    print("---------")
    print(f"{colored(board[6])} | {colored(board[7])} | {colored(board[8])}")
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.CYAN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(0, 9) or board[move] != str(move + 1):
        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except:
            print("Invalid input. Please try again.")
    board[move] = symbol

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol
    
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not s.isdigit() for s in board)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input("Enter your name: ")
    player_symbol, ai_symbol = player_choice()
    board = [str(i + 1) for i in range(9)]
    game_on = True

    while game_on:
        display_board(board)
        if player_symbol == 'X':
            player_move(board, player_symbol)
            if check_win(board, player_symbol):
                display_board(board)
                print(player_name + ", you have won the game!")
                break
            elif check_full(board):
                display_board(board)
                print("It's a tie!")
                break
            ai_move(board, ai_symbol, player_symbol)
            if check_win(board, ai_symbol):
                display_board(board)
                print("AI has won the game!")
                break
            elif check_full(board):
                display_board(board)
                print("It's a tie!")
                break
        else:
            ai_move(board, ai_symbol, player_symbol)
            if check_win(board, ai_symbol):
                display_board(board)
                print("AI has won the game!")
                break
            elif check_full(board):
                display_board(board)
                print("It's a tie!")
                break
            player_move(board, player_symbol)
            if check_win(board, player_symbol):
                display_board(board)
                print(player_name + ", you have won the game!")
                break
            elif check_full(board):
                display_board(board)
                print("It's a tie!")
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        tic_tac_toe()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    tic_tac_toe()
