class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def get_player_move(player_letter, game):
    while True:
        try:
            print(f"\nPlayer {player_letter}'s turn")
            move = int(input(f"Enter position (0-8): "))
            if 0 <= move <= 8:
                if move in game.available_moves():
                    return move
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Position must be between 0 and 8.")
        except ValueError:
            print("Please enter a valid number.")


def play(game, print_game=True):
    if print_game:
        print("Welcome to Tic Tac Toe!")
        print("Positions are numbered from 0 to 8 as shown below:")
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        square = get_player_move(letter, game)

        if game.make_move(square, letter):
            if print_game:
                print(f'\nPlayer {letter} makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'Player {letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    t = TicTacToe()
    play(t, print_game=True)
