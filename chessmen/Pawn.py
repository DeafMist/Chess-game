class Pawn:
    def __init__(self, start_pos, color, img_name):
        self.start_field = start_pos
        self.field = start_pos
        self.color = color
        self.img_name = img_name

    def move(self, final_pos, chessboard):
        if final_pos[0] < 0 or final_pos[0] > 7 or final_pos[1] < 0 or final_pos[1] > 7:
            return False

        if self.field == final_pos:
            return False

        if self.color == 'white':
            if self.field == self.start_field:
                if not (self.field[1] == final_pos[1] and (final_pos[0] - self.field[0] == 1 or final_pos[0] - self.field[0] == 2) or
                        chessboard.board[self.field[0] + 1][self.field[1] - 1].chessman.color == self.color or
                        chessboard.board[self.field[0] + 1][self.field[1] + 1].chessman.color == self.color):
                    return False

            if not (self.field[1] == final_pos[1] and final_pos[0] - self.field[0] == 1 or
                    chessboard.board[self.field[0] + 1][self.field[1] - 1].chessman.color == self.color or
                    chessboard.board[self.field[0] + 1][self.field[1] + 1].chessman.color == self.color):
                return False
        else:
            if self.field == self.start_field:
                if not (self.field[1] == final_pos[1] and (final_pos[0] - self.field[0] == -1 or final_pos[0] - self.field[0] == -2) or
                        chessboard.board[self.field[0] - 1][self.field[1] - 1].chessman.color == self.color or
                        chessboard.board[self.field[0] - 1][self.field[1] + 1].chessman.color == self.color):
                    return False

            if not (self.field[1] == final_pos[1] and final_pos[0] - self.field[0] == -1 or
                    chessboard.board[self.field[0] - 1][self.field[1] - 1].chessman.color == self.color or
                    chessboard.board[self.field[0] - 1][self.field[1] + 1].chessman.color == self.color):
                return False

        is_barrier = False
        cur_pos = self.field

        if self.color == 'white':
            if self.field == self.start_field:
                count = final_pos[0] - self.field[0]
                step = 1

                while step <= count or not is_barrier:
                    if chessboard.board[self.field[0] + step][self.field[1]].chessman is not None:
                        is_barrier = True
                    step += 1
            else:
                if chessboard.board[self.field[0] + 1][self.field[1]].chessman is not None:
                    is_barrier = True
        else:
            if self.field == self.start_field:
                count = self.field[0] - final_pos[0]
                step = 1

                while step <= count or not is_barrier:
                    if chessboard.board[self.field[0] - step][self.field[1]].chessman is not None:
                        is_barrier = True
                    step += 1
            else:
                if chessboard.board[self.field[0] - 1][self.field[1]].chessman is not None:
                    is_barrier = True

        if is_barrier:
            return False
            # self.field = final_pos
        else:
            self.field = final_pos
            return True
