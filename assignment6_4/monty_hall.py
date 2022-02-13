import random


def initialize_doors(number_of_doors):
    random_index = random.randint(1, number_of_doors)
    list = [0.0] * number_of_doors

    for i in range(len(list)):
        if(i == random_index - 1):
            list[i] = True;
        else:
            list[i] = False;
    return list

def initialize_door_numbers(number_of_doors):
    list = [0.0] * number_of_doors

    for i in range(number_of_doors):
        list[i] = i + 1

    return list

def remove_wrong_doors(chosen_door, doors):
    # etsitään ovi jonka totuusarvo on True
    right_door_number = doors.index(True) + 1

    if(chosen_door == right_door_number):
        rand_door = random.randint(1, len(doors))

        while(rand_door == right_door_number):
            rand_door = random.randint(1, len(doors))
        else:
            return rand_door
    else:
        return right_door_number

def print_doors(doors, dont_open):
    print(" _  " * len(doors))

    for i in range(len(doors)):
        if(i != len(doors) - 1):
            if((i+1) not in dont_open):
                if(doors[i]):
                    print("|C|", end=" ")
                else:
                    print("|G|", end=" ")
            else:
                print("| |", end=" ")
        else:
            if((i+1) not in dont_open):
                if(doors[i]):
                    print("|C| ")
                else:
                    print("|G| ")
            else:
                print("| | ")

    for i in range(len(doors)):
        if(i != len(doors) - 1):
            print("|_|", end=" ")
        else:
            print("|_| ")

    for i in range(len(doors)):
        if(i != len(doors) - 1):
            print(f"{str(i+1):^3s}", end=" ")
        else:
            print(f"{str(i+1):^3s} ")
    
    


def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    number_of_doors = int(input("How many doors?\n"))

    while(number_of_doors > 999 or number_of_doors < 3):
        print("The number of doors must be between 3-999!")
        number_of_doors = int(input("How many doors?\n"))

    
    doors = initialize_doors(number_of_doors)
    door_numbers = initialize_door_numbers(number_of_doors)

    print_doors(doors, door_numbers)

    chosen_door = int(input(f"Choose a door 1-{number_of_doors}.\n"))

    while(chosen_door < 1 or chosen_door > number_of_doors):
        chosen_door = int(input(f"Choose a door 1-{number_of_doors}.\n"))

    print(f"You chose the door number {chosen_door}.")
    print("...")

    unopened_doors = []
    result_door = remove_wrong_doors(chosen_door, doors)
    unopened_doors.append(result_door)
    unopened_doors.append(chosen_door)
    print_doors(doors, unopened_doors)

    print(f"{number_of_doors - 2} certainly wrong doors were opened. The door number {result_door} was left.")

    new_door = int(input(f"Choose {chosen_door} if you want to keep the door you first chose and choose {result_door} if you want to change the door.\n"))
    available_doors = [chosen_door, result_door]
    while(new_door not in available_doors):
        new_door = int(input(f"Choose {chosen_door} if you want to keep the door you first chose and choose {result_door} if you want to change the door.\n"))

    print_doors(doors, [])
    
    if(doors[new_door - 1] == True):
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")
    
main()