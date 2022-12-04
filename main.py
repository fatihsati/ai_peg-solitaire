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


def main():
    board = create_peg_solitaire_board()
    print(board)

main()