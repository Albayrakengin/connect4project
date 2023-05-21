import table
import user
class conditions:

    def __init__(self) -> None:
        self.board = table.ussample.gameBoard
        self.rows = 9
        self.cols = 9

    def check_square(self, piece, r, c):
  
        if r < 0 or r >= self.rows:
            return False
        if c < 0 or c >= self.cols:
            return False
        return self.board[r][c] == piece

    def horizontal_win(self, piece, r, c):
        return (
            self.check_square(piece, r, c)
            and self.check_square(piece, r, c + 1)
            and self.check_square(piece, r, c + 2)
            and self.check_square(piece, r, c + 3)
        )

    def vertical_win(self, piece, r, c):

        return (
            self.check_square(piece, r, c)
            and self.check_square(piece, r + 1, c)
            and self.check_square(piece, r + 2, c)
            and self.check_square(piece, r + 3, c)
        )

    def diagonal_win(self, piece, r, c):

        return (
            self.check_square(piece, r, c)
            and self.check_square(piece, r + 1, c + 1)
            and self.check_square(piece, r + 2, c + 2)
            and self.check_square(piece, r + 3, c + 3)
        ) or (
            self.check_square(piece, r, c)
            and self.check_square(piece, r - 1, c + 1)
            and self.check_square(piece, r - 2, c + 2)
            and self.check_square(piece, r - 3, c + 3)
        )

    def winning_move(self, piece):

        for c in range(self.cols):
            for r in range(self.rows):
                if (
                    self.horizontal_win(piece, r, c)
                    or self.vertical_win(piece, r, c)
                    or self.diagonal_win(piece, r, c)
                ):
                    user.user_data.clear_data()
                    return True
        return False

    def tie_move(self):
    
        slots_filled = 0

        for c in range(self.cols):
            for r in range(self.rows):
                if self.board[r][c] != 0:
                    slots_filled += 1

        return slots_filled == 80