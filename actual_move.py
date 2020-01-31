from .board import board
class MoveError(Exception):
    pass # he did this class in class idk if we could actually use it like this

class Move(object):
    def make_move(self): # shouldn't we have the board here too?
        board.update_board(self.row, self.col)
        #if the board isn't in bounds:
            # raise error (Move Error)
            raise MoveError(f"{self.row}, {self.col} is not in bounds, homie!")
        # we will call this update board: board.update_board
        # executing the moves (self.row, self.col)

        return new_board

    def update_board(self): # return new board after each move

    def get_new_board(self):
        return update_board

    def is_in_bounds(self, row: int, col: int) -> bool: # IDK IF we need this but he did it in class




