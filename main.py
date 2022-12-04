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

def move_peg(board, start, end):
    if (start[0] == end[0] and abs(start[1] - end[1]) == 2) or (start[1] == end[1] and abs(start[0] - end[0]) == 2):
        if board[start[0]][start[1]] == 1 and board[end[0]][end[1]] == 0:
            if start[0] == end[0]:
                mid = (start[0], (start[1] + end[1]) // 2)
            else:
                mid = ((start[0] + end[0]) // 2, start[1])
            if board[mid[0]][mid[1]] == 1:
                board[start[0]][start[1]] = 0
                board[mid[0]][mid[1]] = 0
                board[end[0]][end[1]] = 1
                return True
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

def main():
    board = create_peg_solitaire_board()
    moves = get_possible_moves(board)
    print(moves)

main()