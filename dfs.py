from board import Board
from main import *



def main():
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    frontier = [board]
    explored = []
    
    explored_node_count = 0
    while frontier:
        node = frontier.pop(-1)
        explored.append(node)
        explored_node_count += 1
        if check_if_board_is_solved(child.board):
            print('Solution found')
            print('Explored node count: ', explored_node_count)
            print('Solution depth: ', child.depth)
            print_board(child.board)
            return
            
        moves = get_possible_moves(node.board)
        for start, end in moves:
            child = Board(move_peg(node.board, start, end), node, node.depth + 1)
            if child in frontier:
                continue
            frontier.append(child)
        
    
if __name__ == '__main__':
    main()
    