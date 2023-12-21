import copy

ROWS = 6
COLS = 7
AI_PLAYER = 'AI'
HUMAN_PLAYER = 'HU'

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def make_move(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == '-':
            board[row][col] = player    
            return True
    return False

def is_valid_move(board, col):
    if col < COLS and col >= 0:
        return board[0][col] == '-'
    
    return False

def is_game_over(board):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != '-'
            ):
                return True

    for row in range(ROWS - 3):
        for col in range(COLS):
            if (
                board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != '-'
            ):
                return True

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != '-'
            ):
                return True

            if (
                board[row + 3][col] == board[row + 2][col + 1] == board[row + 1][col + 2] == board[row][col + 3] != '-'
            ):
                return True

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == '-':
                return False
    return True

def evaluate_window(window, player):
    score = 0
    opponent = HUMAN_PLAYER if player == AI_PLAYER else AI_PLAYER

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count('-') == 1:
        score += 5
    elif window.count(player) == 2 and window.count('-') == 2:
        score += 2

    if window.count(opponent) == 3 and window.count('-') == 1:
        score -= 4

    return score

def evaluate_state(board):
    score = 0

    # Evaluate each window
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            score += evaluate_window(window, AI_PLAYER)

    for row in range(ROWS - 3):
        for col in range(COLS):
            window = [board[row][col], board[row + 1][col], board[row + 2][col], board[row + 3][col]]
            score += evaluate_window(window, AI_PLAYER)

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2], board[row + 3][col + 3]]
            score += evaluate_window(window, AI_PLAYER)

            window = [board[row + 3][col], board[row + 2][col + 1], board[row + 1][col + 2], board[row][col + 3]]
            score += evaluate_window(window, AI_PLAYER)

    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate_state(board)

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = copy.deepcopy(board)
                make_move(new_board, col, AI_PLAYER)
                eval = minimax(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(COLS):
            if is_valid_move(board, col):
                new_board = copy.deepcopy(board)
                make_move(new_board, col, HUMAN_PLAYER)
                eval = minimax(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = -1

    for col in range(COLS):
        if is_valid_move(board, col):
            new_board = copy.deepcopy(board)
            make_move(new_board, col, AI_PLAYER)
            move_val = minimax(new_board, 4, float('-inf'), float('inf'), False)
            if move_val > best_val:
                best_val = move_val
                best_move = col

    return best_move

board = [
    ['-' for _ in range(COLS)]
    for _ in range(ROWS)
]

print_board(board)  

while not is_game_over(board):
    human_move = int(input("Enter your move (0-6): "))
    if is_valid_move(board, human_move):
        make_move(board, human_move, HUMAN_PLAYER)
        print_board(board)

        if is_game_over(board):
            print("Game Over. You win!")
            break

        ai_move = find_best_move(board)
        make_move(board, ai_move, AI_PLAYER)
        print_board(board)

        if is_game_over(board):
            print("Game Over. AI wins!")
            break
    else:
        print("Invalid move. Try again.")