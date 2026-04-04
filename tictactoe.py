board = {str(i):' ' for i in range(1, 10)}
def print_board():
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print("-+-+-")
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print("-+-+-")
    print(f"{board['1']}|{board['2']}|{board['3']}")

def check_win(t):
    wins = [('7','8','9'), ('4','5','6'), ('1','2','3'),
            ('1','4','7'), ('2','5','8'), ('3','6','9'),
            ('7','5','3'), ('1','5','9')]
    return any(board[a] == board[b] == board[c] == t for a,b,c in wins)

def game():
    turn, count = 'X' , 0
    while count<9:
        print_board()
        move = input(f"turn {turn}, choose position: ")

        if move in board and board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Invalid move!")
            
        if count >= 5 and check_win(turn):
            print_board()
            print(f'\n{turn}wins!')
            break
        turn = '0' if turn == 'X' else 'X'
    else:
        print_board()
        print("\nIts a tie!")
    if input("Play again? (y/n): ").lower() == 'y':
        for k in board: board[k] = ' '
        game()
if __name__ == '__main__':
    game()