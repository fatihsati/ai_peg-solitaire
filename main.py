
# Fatih Satı - 150119625
# Mehmet Selman Baysan - 150120841

# Main operations of the program.
# Creating board, calculating possible moves, moving pegs, checking if board is solved and printing the output.

def print_boards(boards):
    """print the boards in the list in reverse order to get the correct order, from initial board to solution board"""
    for board in reversed(boards): # since boards are stored in reverse order, we need to reverse the list
        for row in board:   
            for each in row:
                if each == -1:      # if the value is -1, print a space instead since -1 is used to represent out of the board.
                    print(' ', end=' ')
                else:
                    print(each, end=' ')  
            print() # print a new line after each row
        print() # print a blank line between boards to make it easier to read

def output_function(method, time_limit, solution_type, remaining_peg, boards, time_spent, explored_node_count, max_number_of_nodes_in_memory, failure_type):
    # board states
    print_boards(boards)
    print(f'Method: {method} - Time limit: {time_limit}')
    if solution_type == 'cutoff':
        print(f'Sub-optimal solution found with {remaining_peg} remaining pegs')
        print(f'No Optimal solution found - {failure_type}')
    else:
        print(f'Optimum solution found.')
    
    print(f'Time spent: {time_spent}')
    print(f'Explored node count: {explored_node_count}')
    print(f'Max number of nodes in memory: {max_number_of_nodes_in_memory}')

def get_parents(node):
    if node.parent is None:
        return [node.board]
    return [node.board] + get_parents(node.parent)

def get_remaining_peg(board):
    return sum(x.count(1) for x in board)

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
