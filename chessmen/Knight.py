class Knight:
    def __init__(self, start_pos, color, img_name):
        self.field = start_pos
        self.color = color
        self.img_name = img_name

    def move(self, final_pos, chessboard):
        if final_pos[0] < 0 or final_pos[0] > 7 or final_pos[1] < 0 or final_pos[1] > 7:
            return False

        if self.field == final_pos:
            return False

        if not (abs(final_pos[0] - self.field[0]) == 2 and abs(final_pos[1] - self.field[1]) == 1 or
                abs(final_pos[0] - self.field[0]) == 1 and abs(final_pos[1] - self.field[1]) == 2):
            return False

        is_barrier = False

        if chessboard.board[final_pos[0]][final_pos[1]].chessman is not None:
            is_barrier = True

        if is_barrier:
            if chessboard.board[final_pos[0]][final_pos[1]].chessman.color != self.color:
                self.field = final_pos
                return True
            return False
            # self.field = final_pos
        else:
            self.field = final_pos
            return True
