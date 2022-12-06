from board import Board
from main import *
import time


def main():
    ALGORITHM = 'BFS'
    TIME_LIMIT = 3600
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    frontier = [board]
    start_time = time.time()
    explored_node_count = 0
    max_node_in_memory = 0
    min_left_peg = 32
    explored_node_count = 0
    
    while frontier:
        if len(frontier) > max_node_in_memory:
            max_node_in_memory = len(frontier)
        node = frontier.pop(0)
        explored_node_count += 1
        if time.time() - start_time >= TIME_LIMIT:
            # time limit exceeded, return message
            time_spent = round(time.time() - start_time, 2)
            board_list = get_parents(node)
            output_function(ALGORITHM, TIME_LIMIT, 'cutoff', min_left_peg, board_list, time_spent, explored_node_count, max_node_in_memory, 'Time Limit')
            return # print the output and stop executing.
        if check_if_board_is_solved(node.board):
            # solution found, return message
            time_spent = round(time.time() - start_time, 2)
            board_list = get_parents(node)
            output_function(ALGORITHM, TIME_LIMIT, 'Optimal', min_left_peg, board_list, time_spent, explored_node_count, max_node_in_memory, 'None')
            return # print the output and stop executing.
        
        # if not solved, check remaining pegs
        left_peg = get_remaining_peg(node.board)
        if left_peg < min_left_peg:
            min_left_peg = left_peg
        moves = get_possible_moves(node.board)
        # get possible moves and add to frontier
        for start, end in moves:
            child = Board(move_peg(node.board, start, end), node, node.depth + 1)
            if child in frontier:
                continue
            frontier.append(child)
           

if __name__ == '__main__':      
    main()