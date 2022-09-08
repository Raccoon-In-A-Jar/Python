class Pawn:
    def __init__(self, x_pos=0, y_pos=0):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def _moveAuthorized(self, board, anotherPawn, rowNbr, colNbr):