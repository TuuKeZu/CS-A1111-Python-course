nopeus_rajoitus = 45 #km/h

def main():
    speed = int(input("Enter your speed in km/h:" + "\n"))

    if(speed >= nopeus_rajoitus):
        print("Oh no, better prepare yourself for a fine.")
    else:
        print("You should be all good.")

    return

main()
    
