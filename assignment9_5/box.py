from math import fabs


class Box:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        self.__owner = None
        self.__left_side = False
        self.__right_side = False
        self.__up_side = False
        self.__down_side = False;

    def get_owner(self):
        return self.__owner

    def add_owner(self, owner):
        self.__owner = owner

    def has_line_on_side(self, side):
        if(side == Box.LEFT):
            return self.__left_side
        elif(side == Box.RIGHT):
            return self.__right_side
        elif(side == Box.UP):
            return self.__up_side
        elif(side == Box.DOWN):
            return self.__down_side

    def add_line(self, side):
        if(self.has_line_on_side(side)):
            return False
        else:
            if(side == Box.LEFT):
                self.__left_side = True
            elif(side == Box.RIGHT):
                self.__right_side = True
            elif(side == Box.UP):
                self.__up_side = True
            elif(side == Box.DOWN):
                self.__down_side = True
            return True
        

    def four_lines_placed(self):
        if( 
            self.has_line_on_side(Box.LEFT) and
            self.has_line_on_side(Box.RIGHT) and
            self.has_line_on_side(Box.UP) and
            self.has_line_on_side(Box.DOWN)
        ):
            return True
        else:
            return False

    def __str__(self):
        value = "["
        for i in range(4):
            value += str(self.__sides[i])
            if(i != 3):
                value += ", "

        value += "]"
        return value


    
        