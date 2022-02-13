from box import Box
import math

class DotsAndBoxesGame:
    TIE = "tie"
    PLAYER1 = "A"
    PLAYER2 = "B"

    def __init__(self, grid_width, grid_height, player_name_1, player_name_2):
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__player_name_1 = player_name_1
        self.__player_name_2 = player_name_2
        self.__grid = self.create_grid()

    def create_grid(self):
        grid = []
        
        for i in range(self.__grid_height):
            grid_row = []

            for e in range(self.__grid_width):
                grid_row.append(Box())
            
            grid.append(grid_row)
        
        return grid

    def add_line(self, x, y, side, player):
        target = self.__grid[x - 1][y - 1]
        added_line = target.add_line(side)
        all_lines_placed = False

        if(added_line):
            self.update_neighbour_of_box(x - 1, y - 1, side)
            neighbor = self.get_neighbour_on_side(side, x - 1, y - 1)

            if(neighbor != None):
                if(target.four_lines_placed()):
                    all_lines_placed = True
                    target.add_owner(player)

                if(neighbor.four_lines_placed()):
                    all_lines_placed = True
                    neighbor.add_owner(player)
            else:
                if(target.four_lines_placed()):
                    all_lines_placed = True
                    target.add_owner(player)

        return added_line, all_lines_placed

    def calculate_points_of_player(self, player):
        points = 0
        for i in range(self.__grid_height):
            for e in range(self.__grid_width):
                box = self.__grid[i][e]

                if(box.four_lines_placed()):
                    if(box.get_owner() == player):
                        points += 1
        return points

    def is_ended(self):
        boxes = 0
        number_of_boxes = self.__grid_height * self.__grid_width
        for i in range(self.__grid_height):
            for e in range(self.__grid_width):
                box = self.__grid[i][e]
                if(box.four_lines_placed()):
                    boxes += 1

        return boxes == number_of_boxes

    def winner(self):
        p1 = self.calculate_points_of_player(self.__player_name_1)
        p2 = self.calculate_points_of_player(self.__player_name_2)

        if(p1 == p2):
            return self.TIE

        if(p1 > p2):
            return self.__player_name_1

        if(p2 > p1):
            return self.__player_name_2

    def give_score(self):
        result = "\nScore:\n\n"
        result += "{:<15s} | {:<15s}\n".format(f"{self.__player_name_1} ({self.PLAYER1})", f"{self.__player_name_2} ({self.PLAYER2})")
        result += "-" * 37
        result += "\n{:<15s} | {:<15s}\n".format(f"{self.calculate_points_of_player(self.__player_name_1)}", f"{self.calculate_points_of_player(self.__player_name_2)}")
        
        return result

    

                


    def update_neighbour_of_box(self, row_index, column_index, side):
        neighbor = self.get_neighbour_on_side(side, row_index, column_index)

        if(neighbor != None):
            if(side == Box.LEFT):
                neighbor.add_line(Box.RIGHT)
            elif(side == Box.RIGHT):
                neighbor.add_line(Box.LEFT)
            elif(side == Box.UP):
                neighbor.add_line(Box.DOWN)
            elif(side == Box.DOWN):
                neighbor.add_line(Box.UP)


    def get_neighbour_on_side(self, side, row, column):
        grid = self.__grid
        neighbor = None
        if(side == Box.LEFT):
            try:
                if(column - 1 < 0):
                    return None
                neighbor = grid[row][column - 1]
            except IndexError:
                return None
        elif(side == Box.RIGHT):
            try:
                neighbor = neighbor = grid[row][column + 1]
            except IndexError:
                return None
        elif(side == Box.UP):
            try:
                if(row - 1 < 0):
                    return None
                neighbor = neighbor = grid[row - 1][column]
            except IndexError:
                return None
        elif(side == Box.DOWN):
            try:
                neighbor = grid[row + 1][column]
            except IndexError:
                return None
        return neighbor

    def one_row_of_grid(self, row_index):
        column = self.__grid[math.floor(row_index / 2)]
        s = ""

        
        if(row_index % 2 == 0):
            s += "   o"

            for i in range(self.__grid_width):
                box = column[i]
                if(box.has_line_on_side(Box.UP)):
                    s += " —— o"
                else:
                    s += "    o"
            s += "\n"
        else:
            for i in range(self.__grid_width):
                box = column[i]
                c = "****"
                # check wather the box has all sides filled or not
                if(box.four_lines_placed()):
                    player = box.get_owner()
                    o = "E"
                    if(player == self.__player_name_1):
                        o = "A"
                    elif(player == self.__player_name_2):
                        o = "B"
                    
                    c = f"*{o}**"
                else:
                    c = "****"

                if(i == (self.__grid_width - 1)):
                    lines = [box.has_line_on_side(Box.LEFT), box.has_line_on_side(Box.RIGHT)]
    
                    if(lines[0] and lines[1]):
                        s += f"|{c}|"
                    elif(lines[0] and not lines[1]):
                        s += f"|{c}"
                    elif(not lines[0] and lines[1]):
                        s += f"*{c}|"
                    else:
                        s += f"*{c}"
                else:
                    if(box.has_line_on_side(Box.LEFT)):
                        s += f"|{c}"
                    else:
                        s += f"{c}*"

            s += "\n"
            
        return s.replace('*', ' ')

    def final_row_of_grid(self):
        column = self.__grid[self.__grid_height - 1]
        s = ""
        s += "   o"
        for i in range(self.__grid_width):
            
            box = column[i]
            if(box.has_line_on_side(Box.DOWN)):
                s += " —— o"
            else:
                s += "    o"
        s += "\n"

        return s
    
    def __str__(self):
        rows = self.__grid_height
        result = ""
        row_num = 0

        first_row = "**"

        for i in range(self.__grid_width):
            first_row += f"****{i + 1}"
        
        result += f"{first_row} \n"
        for i in range(rows * 2):

            if(i % 2 != 0):
                result += f"{math.floor(row_num / 2) + 1}  " + self.one_row_of_grid(row_num)
            else:
                result += self.one_row_of_grid(row_num)
            
            row_num += 1
        
        result += self.final_row_of_grid()
        result += self.give_score()

        
        return result.replace('*', ' ')





    
