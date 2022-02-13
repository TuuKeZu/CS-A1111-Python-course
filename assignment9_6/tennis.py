def calculatePoints(number_of_points):
    if(number_of_points <= 2):
        return 15 * number_of_points
    elif(number_of_points == 3):
        return 40
    else:
        return -1

def printScores(p1_points, p2_points):

    p1 = calculatePoints(p1_points)
    p2 = calculatePoints(p2_points)

    print(f"Score: {p1} - {p2}")

def printDeuce(p1_points, p2_points):
    p1 = calculatePoints(p1_points)
    p2 = calculatePoints(p2_points)

    if(p1 == p2):
        print("Deuce")


def main():
    print("This program calculates tennis scores.")
    has_ended = False;

    player_1 = input("Enter server's name.\n")
    player_2 = input("Enter receiver's name.\n")

    p1_points = 0;
    p2_points = 0;
    p1_advantage = False
    p2_advantage = False
    deuse = False

    while(not has_ended):
        point = int(input(f"Who won the point?\n1. {player_1}\n2. {player_2}\n"))
        
        if(point == 1 or point == 2):
            if(point == 1):
                if(calculatePoints(p1_points + 1) != -1):
                    p1_points += 1
                    printScores(p1_points, p2_points) 
                    printDeuce(p1_points, p2_points)
                else:
                    if(not deuse):
                        has_ended = True
                        print(f"Game ended. The winner is {player_1}.")
                        return
                    if(p1_advantage):
                        has_ended = True
                        print(f"Game ended. The winner is {player_1}.")
                        return
                    else:
                        if(p2_advantage):
                            printScores(p1_points, p2_points)
                            print("Deuce.")
                            p2_advantage = False
                        else:
                            printScores(p1_points, p2_points)
                            print("Advantage in.")
                            p1_advantage = True
            if(point == 2):
                if(calculatePoints(p2_points + 1)  != -1):
                    p2_points += 1
                    printScores(p1_points, p2_points)
                    printDeuce(p1_points, p2_points)
                else:
                    if(not deuse):
                        has_ended = True
                        print(f"Game ended. The winner is {player_2}.")
                        return
                    if(p2_advantage):
                        has_ended = True
                        print(f"Game ended. The winner is {player_2}.")
                        return
                    else:
                        if(p1_advantage):
                            printScores(p1_points, p2_points)
                            print("Deuce.")
                            p1_advantage = False
                        else:
                            printScores(p1_points, p2_points)
                            print("Advantage out.")
                            p2_advantage = True


        else:
            print("ERROR: Invalid number.")
            printScores(p1_points, p2_points)

        p1 = calculatePoints(p1_points)
        p2 = calculatePoints(p2_points)

        if(p1 == 40 and p2 == 40):
            deuse = True



main()