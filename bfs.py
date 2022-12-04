from main import *
from board import Board

def print_board(board_to_print):
    if not board_to_print:
        print('No solution found')
        return
    for row in board_to_print:
        print(row)
        

def main():
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    print(type(board))
    frontier = [board]
    explored = []
    
    
    while frontier:
        node = frontier.pop(0)
        explored.append(node)
        moves = get_possible_moves(node.board)
        # if not moves:
        #     print('No solution on this path')
        for start, end in moves:
            child_board = move_peg(node.board, start, end)
            child = Board(child_board, node, node.depth + 1)
            if child in explored or child in frontier:
                continue
            # if child.state is goal, return solution
            if check_if_board_is_solved(child_board):
                print('Solution found')
                return
            frontier.append(child)
           
    print_board(child_board)
        
main()