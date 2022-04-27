class Queen:
    def __init__(self, start_pos, color, img_name):
        self.field = start_pos
        self.color = color
        self.img_name = img_name

    def move(self, final_pos, chessboard):
        if final_pos[0] < 0 or final_pos[0] > 7 or final_pos[1] < 0 or final_pos[1] > 7:
            return False

        if self.field == final_pos:
            return False

        if not (self.field[0] == final_pos[0] or self.field[1] == final_pos[1] or
                abs(final_pos[0] - self.field[0]) == abs(final_pos[1] - self.field[1])):
            return False

        is_barrier = False
        cur_pos = self.field

        if abs(final_pos[0] - self.field[0]) == abs(final_pos[1] - self.field[1]):
            if final_pos[0] - self.field[0] < 0 and final_pos[1] - self.field[1] < 0:
                step = [-1, -1]
            elif final_pos[0] - self.field[0] < 0 < final_pos[1] - self.field[1]:
                step = [-1, 1]
            elif final_pos[0] - self.field[0] > 0 > final_pos[1] - self.field[1]:
                step = [1, -1]
            elif final_pos[0] - self.field[0] > 0 and final_pos[1] - self.field[1] > 0:
                step = [1, 1]
        else:
            if final_pos[0] - self.field[0] < 0:
                step = [-1, 0]
            elif final_pos[0] - self.field[0] > 0:
                step = [1, 0]
            elif final_pos[1] - self.field[1] < 0:
                step = [0, -1]
            elif final_pos[1] - self.field[1] > 0:
                step = [0, 1]

        while cur_pos != final_pos or not is_barrier:
            cur_pos += step
            if chessboard[cur_pos[0]][cur_pos[1]]:
                is_barrier = True

        if is_barrier:
            if cur_pos == final_pos and chessboard.board[cur_pos[0]][cur_pos[1]].chessman.color != self.color:
                self.field = final_pos
                return True
            return False
            # self.field = final_pos
        else:
            self.field = final_pos
            return True
