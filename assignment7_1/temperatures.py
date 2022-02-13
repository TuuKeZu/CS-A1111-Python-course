def main():
    name = input("Enter a filename:\n")
    count = 0
    try:
        tempfile = open(name, "r")

        for line in tempfile:
            line = line.rstrip()
            temperature = float(line)

            if(temperature < 0):
                count += 1
            
        tempfile.close()
        if count == 0:
            print("There were no temperatures below the freezing point.")
        else:
            print(f"{count} temperatures were below the freezing point.")
    except OSError:
        print("Error in reading file {:s}. Closing program.".format(name))
    except ValueError:
        print("Incorrect line in file {:s}. Closing program.".format(name))


main()