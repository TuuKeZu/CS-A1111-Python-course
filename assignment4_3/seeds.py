BEAN_ROW_SPACING = 50  # cm
BEAN_SEED_SPACING = 15  # cm

RADISH_ROW_SPACING = 20  # cm
RADISH_SEED_SPACING = 4   # cm

CARROT_ROW_SPACING = 30  # cm
CARROT_SEED_SPACING = 2  # cm

def calculate_number_of_seeds(x, y, germination_rate, row_spacing, seed_spacing):
    seeds_per_row = int(y) // int(seed_spacing);
    number_of_rows = int(x) // int(row_spacing);
    print(number_of_rows * seeds_per_row)
    number_of_seeds = number_of_rows * seeds_per_row;
    total_number_of_seeds = number_of_seeds / (germination_rate / 100)
    return int(total_number_of_seeds);

def main():
    print("This program calculates the number of seeds that you need.")
    x = int(input("Enter the width of the field (cm):\n"))
    y = int(input("Enter the height of the field (cm):\n"))
    type = int(input("Which vegetable do you want to grow?\n1. Beans\n2. Radishes\n3. Carrots\n"))
    germination_rate = float(input("Enter the germination rate of the seeds (%):\n"))

    row_spacing = 0;
    seed_spacing = 0;

    if(type == 1):
        row_spacing = BEAN_ROW_SPACING;
        seed_spacing = BEAN_SEED_SPACING;
    elif(type == 2):
        row_spacing = RADISH_ROW_SPACING;
        seed_spacing = RADISH_SEED_SPACING;
    elif(type == 3):
        row_spacing = CARROT_ROW_SPACING;
        seed_spacing = CARROT_SEED_SPACING;

    seeds_x = calculate_number_of_seeds(x, y, germination_rate, row_spacing, seed_spacing)
    seeds_y = calculate_number_of_seeds(y, x, germination_rate, row_spacing, seed_spacing)

    if(seeds_x == seeds_y):
        print("Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.")
        print("You need "+str(seeds_x)+" seeds.")
        return
    
    if(seeds_x < seeds_y):
        print("Set the rows perpendicular to the height ("+str(y)+" cm) of the field to get maximum harvest.")
        print("You need "+str(seeds_y)+" seeds.")
        return
    else:
        print("Set the rows perpendicular to the width ("+str(x)+" cm) of the field to get maximum harvest.")
        print("You need "+str(seeds_x)+" seeds.")
        return


print(calculate_number_of_seeds(300, 500, 90.0, 50, 15))
    