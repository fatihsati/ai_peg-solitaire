
def print_board(board_to_print):
    if not board_to_print:
        print('No solution found')
        return
    for row in board_to_print:
        print(row)

def create_peg_solitaire_board():
    board = []
    for row in range(7):
        board.append([])
        for col in range(7):
            if row in [0,1,5,6] and col in [0,1,5,6]:
                board[row].append(-1)
            elif (row == 3 and col == 3):
                board[row].append(0)
            else:
                board[row].append(1)
    return board

def check_if_board_is_solved(board):
    """Return True if there are only 1 piece left on the board, else return False"""
    peg_number = sum(x.count(1) for x in board)
    if peg_number == 1 and board[3][3] == 1:
        return True
    return False

def move_peg(board, start, end):
    new_board = list(map(list, board))
    if (start[0] == end[0] and abs(start[1] - end[1]) == 2) or (start[1] == end[1] and abs(start[0] - end[0]) == 2):
        if new_board[start[0]][start[1]] == 1 and new_board[end[0]][end[1]] == 0:
            if start[0] == end[0]:
                mid = (start[0], (start[1] + end[1]) // 2)
            else:
                mid = ((start[0] + end[0]) // 2, start[1])
            if new_board[mid[0]][mid[1]] == 1:
                new_board[start[0]][start[1]] = 0
                new_board[mid[0]][mid[1]] = 0
                new_board[end[0]][end[1]] = 1
                return new_board
    return False

def get_possible_moves(board):
    moves = []
    for row in range(7):
        for col in range(7):
            if board[row][col] == 1:
                if row > 1 and board[row - 1][col] == 1 and board[row - 2][col] == 0:
                    moves.append(((row, col), (row - 2, col)))
                if row < 5 and board[row + 1][col] == 1 and board[row + 2][col] == 0:
                    moves.append(((row, col), (row + 2, col)))
                if col > 1 and board[row][col - 1] == 1 and board[row][col - 2] == 0:
                    moves.append(((row, col), (row, col - 2)))
                if col < 5 and board[row][col + 1] == 1 and board[row][col + 2] == 0:
                    moves.append(((row, col), (row, col + 2)))
    return moves
