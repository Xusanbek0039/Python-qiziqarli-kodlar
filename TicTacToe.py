board = [' ' for _ in range(9)]

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def uyin():
    current_player = 'X'
    while True:
        print_board()
        position = int(input("Raqam bilan belgilang(1-9): ")) - 1
        if board[position] == ' ':
            board[position] = current_player
            if check_win(current_player):
                print_board()
                print(f"{current_player} uyinchi yutdi!")
                break
            elif ' ' not in board:
                print_board()
                print("Durrang")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Notugri belgilash, qayta urining!")
uyin()
