import math

VITAMIN_DICTIONARY = {'A': 800, 'B1': 1200, 'B2': 1300, 'B3': 15000, 'B5': 5000,'B6': 1500, 'B12': 2.0,
'C': 75000, 'D': 10, 'E': 9000}

VITAMIN_DATA = {}

def main():
    file_name = input("Enter the name of the food file.\n")
    file_name_parsed = file_name.split('.')[0]
    try:
        file = open(file_name)
        for line in file.readlines():
            data = line.strip().split(' ')
            
            if(len(data) == 2):
                vitamin_name = data[0]

                try:
                    vitamin_value = float(data[1])

                    VITAMIN_DATA[vitamin_name] = vitamin_value

                except ValueError:
                    print(f"Invalid amount of vitamin {vitamin_name}.")


        target_vitamin = input("Enter the vitamin.\n")

        if(target_vitamin in VITAMIN_DATA.keys()):
            amount_in_food = VITAMIN_DATA[target_vitamin]
            if(target_vitamin in VITAMIN_DICTIONARY.keys()):
                amount_needed_for_day = VITAMIN_DICTIONARY[target_vitamin]
                
                vitamin_needed = (amount_needed_for_day / amount_in_food) * 100

                if(vitamin_needed > 1000):
                    print(f"You have to eat {file_name_parsed} {(vitamin_needed / 1000):.1f} kilos to reach the daily recommendation of the vitamin {target_vitamin}.")
                else:
                    print(f"You have to eat {file_name_parsed} {vitamin_needed:.1f} grams to reach the daily recommendation of the vitamin {target_vitamin}.")
            else:
                print(f"{target_vitamin} is an unknown vitamin.")

        else:
            print(f"{file_name_parsed} does not contain any vitamin {target_vitamin}.")

    except OSError:
        print(f"Error in reading {file_name} file.")

main()