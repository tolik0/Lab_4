class Chess:
    """
    Class which represent chess game
    """
    def __init__(self):
        self.board = Board()
        # this parameter can be 0, or 1
        self.current_player = 0


class Board:
    """
    Class which represent chess board
    """
    def __init__(self):
        # list with figures
        self.figures = [Figure("type", (1, 1))]


class Figure:
    """
    Class which represent figure
    """
    def __init__(self, type, coor):
        self.coor = coor
        self.__type = type

    def move(self, coor):
        # key is figure type, value is list with coordinates, how it can move
        figure_type = {"name_of_figure": []}
        if coor in figure_type[self.__type]:
            self.coor[0] += coor[0]
            self.coor[1] += coor[1]
        else:
            print("This figure can't move so")
            self.move()
