import math

PRICE_PER_CUBIC_METER = 5.0  # eur/m^3

def calculate_water_volume_and_price(diameter, height):
    # A = Pr^2

    A = math.pi * (diameter / 2) ** 2;
    volume = A * height;
    price = volume * PRICE_PER_CUBIC_METER

    print(f"You need {(volume*1000):.0f} liters of water to fill the pool.");
    print(f"It will cost you {price:.2f} euros.\n")

def main():
    number_of_pools = int(input("Enter the number of pools:\n"))

    for i in range(number_of_pools):
        cur_pool = (i + 1);

        print(str(cur_pool) + ". pool")

        d = float(input("Enter the diameter of the pool in meters:\n"))
        h = float(input("Enter the diameter of the pool in meters:\n"))
        calculate_water_volume_and_price(d, h)



main()