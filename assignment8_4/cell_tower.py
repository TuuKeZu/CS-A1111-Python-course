import math

test_points = [[[50,100],50], [[200,200],100]]

TOWERS = []

def is_inside_cell_tower_range(point, cell_tower_list):
    for tower in cell_tower_list:
        coords = tower[0]
        range = tower[1]
        x2 = coords[0]
        y2 = coords[1]
        x1 = point[0]
        y1 = point[1]

        dis = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
        if(dis <= range):
            return True
        
    return False


def find_nearest_tower_in_range(point, cell_tower_list):
    in_range = []
    best_tower = []
    closest = float('inf')

    for tower in cell_tower_list:
        coords = tower[0]
        range = tower[1]
        x2 = coords[0]
        y2 = coords[1]
        x1 = point[0]
        y1 = point[1]

        dis = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)

        if(dis <= range):
            in_range.append([tower, dis])

    
    if(len(in_range) == 0):
        return [-1, -1]

    for tower in in_range:
        coords = tower[0]
        dis = tower[1]

        if(dis < closest):
            closest = dis
            best_tower = coords
    return best_tower[0]



def isInteger(string):
    try:
        value = int(string)
        return True
    except ValueError:
        return False

def main():
    file_name = input("Enter the name of the file containing the cell tower information:\n")
    
    try:
        file = open(file_name, "r")
        lines = file.readlines()

        for i in range(len(lines)):
            if(i != 0):
                line = lines[i].strip()
                data = line.split(":")

                if(len(data) == 2):
                    coords = data[0].split(",")

                    if(len(coords) == 2):
                        try:
                            x = int(coords[0])
                            y = int(coords[1])
                            ran = int(data[1])

                            data_object = [[x, y], ran]

                            TOWERS.append(data_object)
                        except ValueError:
                            print(f"Invalid coordinates or radius in line: {line}")
                    else:
                        print(f" Invalid coordinates or radius in line: {line}")
                else:
                    print(f"Invalid line: {line}")
    except OSError:
        print(f"Error in reading the file '{file_name}'.\n")
        print("No cell tower information available.")
        print("Program ends.")
        return
    
    print("File read.\n")

    if(len(TOWERS) == 0):
        print("No cell tower information available.")
        print("Program ends.\n")
        return
    
    print("Enter coordinates. Stop with an empty line.")
    are_valid = False

    coords_s = input("Enter the coordinates separated by comma:\n")

    while(coords_s != ""):
        while(not are_valid):
            are_valid = True
            coords_array = coords_s.split(",")

            if(len(coords_array) != 2):
                print("Invalid coordinates! Enter two coordinates separated by comma.")
                coords_s = input("Enter the coordinates separated by comma:\n")
                are_valid = False

            elif(not isInteger(coords_array[0]) or not isInteger(coords_array[1])):
                print("Invalid coordinates! Enter the coordinates as integers.")
                coords_s = input("Enter the coordinates separated by comma:\n")
                are_valid = False

            elif(int(coords_array[0]) < 0 or int(coords_array[1]) < 0):
                print("Invalid coordinates! Coordinates must be positive integers.")
                coords_s = input("Enter the coordinates separated by comma:\n")
                are_valid = False

            if(coords_s == ""):
                print("Program ends.\n")
                return

        else:
            point = [int(coords_array[0]), int(coords_array[1])]

            is_in_range = is_inside_cell_tower_range(point, TOWERS)
            if(is_in_range):
                print("The place is inside a cellular network range.")
                closest_tower = find_nearest_tower_in_range(point, TOWERS)
                print(f"The coordinates of the cell tower with the strongest signal: ({closest_tower[0]}, {closest_tower[1]})")
            else:
                print("The place is not inside of any cell tower range.")
            
            print()
            coords_s = input("Enter the coordinates separated by comma:\n")
            are_valid = False

    else:
        print("Program ends.\n")
        return
            

main()







