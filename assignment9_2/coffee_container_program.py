# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius, modified by Veera Laine
# Template for Exercise 9.2 Coffee containers

from container import LiquidContainer

def main():
    # Ask the names and volumes of the containers according to the example runs and
    # create three containers: large coffee cup, small coffee cup, and coffee jug.

    B_input = input("Big coffee cup name and volume: ")
    B_data = B_input.split("/")
    S_input = input("Small coffee cup name and volume: ")
    S_data = S_input.split("/")
    J_input = input("Coffee jug name and volume: ")
    J_data = J_input.split("/")

    # creating the classes
    b_cup = LiquidContainer(B_data[0], float(B_data[1]), False)
    s_cup = LiquidContainer(S_data[0], float(S_data[1]), False)
    c_jug = LiquidContainer(J_data[0], float(J_data[1]), True)


    # Print here the statuse of the three created coffee containers
    print("Created the following containers:")
    print(b_cup)
    print(s_cup)
    print(c_jug)
    
    

    # Fill the format with the jug name" 
    print("\nFilling {}...".format(c_jug.get_name()))
    
    # Fill here the coffee jug
    c_jug.fill()

    print("Jug status after filling:")
    # Print here the status of the coffee jug
    print(c_jug)
    
    amount_to_be_served = float(input("\nHow many litres of coffee should be served?\n"))

    # Fill the format. Sould print "Trying to pour [amount to be served] litres from [jug name] into [big cup name] and [small cup name]"
    print("Trying to pour {} litres from {} into {} and {}".format(amount_to_be_served, c_jug.get_name(), b_cup.get_name(), s_cup.get_name())) # This should print 
    poured_in_b = c_jug.pour_to_another(b_cup, amount_to_be_served)
    poured_in_s = c_jug.pour_to_another(s_cup, amount_to_be_served)
    # Pour here the coffee from the jug first to the big cup and then to small cup

    # Print the amounts of the coffee poured in each container, i.e., fill the format
    print("Managed to pour {} litres to {}".format(poured_in_b, b_cup.get_name()))
    print("Managed to pour {} litres to {}".format(poured_in_s, s_cup.get_name()))
  
    print("\nCup and jug statuses after pouring:")
    # Print here the statuses of the containers
    print(b_cup)
    print(s_cup)
    print(c_jug)

    difference = (b_cup.get_liquid_volume() - s_cup.get_liquid_volume())
    
    # Check whether both cups got the same amount of coffee, i.e. fill the if clause
    if (difference == 0):
        print("\nBoth were happy for having the same amount of coffee and lived happily everafter.")
    else:
        # Fill the format with the name of the small cup.
        print("\nThe holder of {} became angry for having less coffee and flipped their coffee cup!".format(s_cup.get_name()))
        
        # Flip here the small cup
        s_cup.flip()
        print("\nThey also flipped the jug!")
        # Flip here the coffee jug
        c_jug.flip()
        print("However, it had a lid, so the liquid stayed inside:")
        # Print here the status of the coffee jug
        print(c_jug)

        print("\nSo they had to force flip to the jug!")
        # Force flip here the coffee jug
        c_jug.force_flip()
        
        print("Now it's empty and no longer has a lid:")
        # Print here the status of the coffee jug
        print(c_jug)

        # Fill the format with the name of the big cup
        print("\nNext they got mad and nicked all the coffee they could from {}".format(b_cup.get_name()))

        # Pour here as much coffee as possible from the large cup to the small cup
        amount_stolen = s_cup.fill_from(b_cup)
        # Fill the format with the stolen amount
        print("{} litres were stolen.".format(amount_stolen))
       
        print("\nCup statuses after the theft:")
        # Print here the status of the big and small cup
        print(b_cup)
        print(s_cup)

        # Fill the format with the name of the small cup
        print("\nNow finally the holder of {} can drink their coffee:".format(s_cup.get_name()))
        # Empty here the small cup
        s_cup.flip()
        # Print here the status of the small cup
        print(s_cup)
    
main()
