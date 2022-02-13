surface_area = 0; #m2
spreading_rate = 0; #m2 / l
number_of_coats = 0; #int
liter_prize = 0; # eur/l

def CalcCost():
    #maarin riittoisuutta voidaan kuvata funktiolla x = A/y, missä x on tarvitavan maalin määrä, y maalin riittoisuus, ja A maalattavan alueen pinta-ala.

    required_liters_for_one_coat = surface_area / spreading_rate #l
    total_liters_required = number_of_coats * required_liters_for_one_coat
    total_cost = liter_prize * total_liters_required

    return("The estimated cost of the paint is " + str(total_cost) + " eur")

print("Enter the area of surface(s) to be painted (m2).")
surface_area = float(input())
print("Enter the spreading rate of the paint (m2/l).")
spreading_rate = float(input())
print("Enter the number of coats.")
number_of_coats = int(input())
print("Enter the prize of the paint (eur/l).")
liter_prize = float(input())

print(CalcCost())