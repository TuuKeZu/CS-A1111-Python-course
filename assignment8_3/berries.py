BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]
BERRY_DATA = {}
BERRY_PRICES = {}

def read_file_data(file_name):
    try:
        file = open(file_name)
        lines = file.readlines()

        for i in range(len(lines)):
            if(i != 0):
                line = lines[i].strip()

                if(line != ""):
                    data = line.split(',')

                    if(len(data) == 3):
                        name = data[1]

                        if(name in BERRY_TYPES):
                            try:
                                amount = int(data[2])

                                if(name in BERRY_DATA.keys()):
                                   BERRY_DATA[name] += amount 
                                else:
                                    BERRY_DATA[name] = amount

                            except ValueError:
                                print(f"Invalid line: {line}")
                        else:
                            print(f"Invalid line: {line}")

                    else:
                        print(f"Invalid line: {line}")

    except:
        print(f"Invalid file: {file_name}")
        print("\nProgram ends.")
        return -99

    file.close()
    return 200

def read_file_prices(file_name):
    try:
        file = open(file_name)
        lines = file.readlines()

        for i in range(len(lines)):
            if(i != 0):
                line = lines[i].strip()

                if(line != ""):
                    data = line.split(':')

                    if(len(data) == 2):
                        name = data[0]

                        if(name in BERRY_TYPES):
                            try:
                                amount = float(data[1])
                                BERRY_PRICES[name] = amount

                            except ValueError:
                                print(f"Invalid line: {line}")
                        else:
                            print(f"Invalid line: {line}")

                    else:
                        print(f"Invalid line: {line}")

    except:
        print(f"Invalid file: {file_name}")
        print("\nProgram ends.")
        return -99

    file.close()
    return 200

def validate_price_list(berry_data, berry_list):
    for berry in berry_data.keys():
        if(berry not in berry_list):
            return -99
    
    return 200

def print_receipt():
    total = 0
    total_kg = 0

    print("\nBerry type   Picked berries (kg)   Money earned (eur)")
    print("-" * 53)
    for berry in BERRY_DATA.keys():
        amount = BERRY_DATA[berry]
        price = BERRY_PRICES[berry]
        earned = amount * price
        print("{:12s} {:>19s} {:>20s}".format(berry, f"{amount:.0f}", f"{earned:.2f}"))



        total += earned
        total_kg += amount

    print("-" * 53)
    print("{:12s} {:>19s} {:>20s}".format(f"Total", f"{total_kg:.0f}", f"{total:.2f}"))
    print("\n\nProgram ends.")


def main():
    file_name = input("Enter the name of the file containing the berry data:\n")
    response = read_file_data(file_name)

    if(response == -99):
        return

    if(response == 200):
        print("File read.")

    file_name = input("Enter the name of the file containing the prices of the berries:\n")
    response = read_file_prices(file_name)

    if(response == -99):
        return

    if(response == 200):
        print("File read.")

    response = validate_price_list(BERRY_DATA, BERRY_PRICES)
    if(response == -99):
        print(f"Some of the berry prices are missing from the file '{file_name}'.")
        print("\nProgram ends.")
        return

    print_receipt()

    





main()