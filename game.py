class TicTacToe:
    def __init__(self):
        pass
    
    def print_board(self):
        # Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Tells us 0 | 1 | 2 what number corresponds to what box
        number_board = [[star[i] for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
           print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']