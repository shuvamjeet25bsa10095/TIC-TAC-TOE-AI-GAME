def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 3)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_max, alpha, beta):
    if is_winner(board, 'O'):
        return 10 - depth
    if is_winner(board, 'X'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_max:
        max_eval = -float('inf')
        for row, col in get_empty_positions(board):
            board[row][col] = 'O'
            eval_score = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = ' '
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row, col in get_empty_positions(board):
            board[row][col] = 'X'
            eval_score = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = ' '
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for row, col in get_empty_positions(board):
        board[row][col] = 'O'
        score = minimax(board, 0, False, -float('inf'), float('inf'))
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            best_move = (row, col)
    if best_move:
        make_move(board, best_move[0], best_move[1], 'O')

def main():
    board = init_board()
    print("Welcome to Tic-Tac-Toe! You are X, AI is O. Enter row col (0-2).")
    while True:
        print_board(board)
        row, col = map(int, input("Your move: ").split())
        if not make_move(board, row, col, 'X'):
            print("Invalid move!")
            continue
        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break
        ai_move(board)
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

if __name__ == "__main__":
    main()