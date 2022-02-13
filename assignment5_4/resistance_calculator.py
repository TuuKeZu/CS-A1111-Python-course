def resistors_in_parallel(resistor_list, target):
    possible_pairs = []
    best_resistance = 999
    result = [];
    min_target = (1/target) - (1/target) * 0.02 # 2%
    max_target = (1/target) + (1/target) * 0.02 # 2%

    for res1 in resistor_list:
        for res2 in resistor_list:
            resistance = (1/res1) + (1/res2);
            
            if(resistor_list.count(res1) == 1 and res1 == res2):
                possible_pairs = possible_pairs
            else:
                if(resistance >= min_target and resistance <= max_target):
                    possible_pairs.append([float(res1), float(res2)])

    # if there aren't any pairs that match the target
    if(len(possible_pairs) == 0):
        return(0.0, 0.0, 0.0)
    
    else:

        # list through every pair's resistance, and sort them to find out which one is closest to the target
        for p in possible_pairs:
            resistance = 1 / ( 1 / p[0] + 1 / p[1])
            difference = abs(target - resistance);
            

            # see if the difference is less than current best one

            if(difference < best_resistance):
                best_resistance = resistance;
                resistors = [p[0], p[1]]
                resistors.sort(reverse=True)
                result = [resistance, resistors[0], resistors[1]]

        return(result[0], result[1], result[2])

def resistors_in_series(resistor_list, target):
    # käytetään yleistä parinetsintä-algorytmiä (kaksi looppia)
    possible_pairs = []
    best_resistance = 999
    result = [];
    min_target = target - target * 0.02 # 2%
    max_target = target + target * 0.02 # 2%

    for res1 in resistor_list:
        for res2 in resistor_list:
            resistance = res1 + res2;
            
            if(resistor_list.count(res1) == 1 and res1 == res2):
                possible_pairs = possible_pairs
            else:
                if(resistance >= min_target and resistance <= max_target):
                    possible_pairs.append([float(res1), float(res2)])

    # if there aren't any pairs that match the target
    if(len(possible_pairs) == 0):
        return(0.0, 0.0, 0.0)
    
    else:

        # list through every pair's resistance, and sort them to find out which one is closest to the target
        for p in possible_pairs:
            resistance = p[0] + p[1]
            difference = abs(target - resistance);

            # see if the difference is less than current best one

            if(difference < best_resistance):
                best_resistance = resistance;
                resistors = [p[0], p[1]]
                resistors.sort(reverse=True)
                result = [resistance, resistors[0], resistors[1]]

        return(result[0], result[1], result[2]);

def main():
    resistor_list = []
    target = float(input("Enter the desired resistance in ohms.\n"))
    resistor = float(input("Enter the resistances of the resistors in ohms and stop with a negative value.\n"))

    while(resistor >= 0):
        resistor_list.append(resistor)
        resistor = float(input())
    else:

        parallel = resistors_in_parallel(resistor_list, target)
        series = resistors_in_series(resistor_list, target)
        
        # jos rinnan ei toimi
        if(parallel == (0.0, 0.0, 0.0) or series == (0.0, 0.0, 0.0)):
            # tarkistetaan, toimiiko rinnan
            if(series == (0.0, 0.0, 0.0) and parallel == (0.0, 0.0, 0.0)):
                # ratkaisua ei ole
                print("No suitable resistors.")
                return
            elif(parallel == (0.0, 0.0, 0.0) and series != (0.0, 0.0, 0.0)):
                # series one is better
                resistors = [series[1], series[2]]
                print(f"The best combination of resistors is {resistors[0]:.1f} ohm and {resistors[1]:.1f} ohm resistors connected in series.")
                return
            elif(parallel != (0.0, 0.0, 0.0) and series == (0.0, 0.0, 0.0)):
                # parallel one is better
                resistors = [parallel[1], parallel[2]]
                print(f"The best combination of resistors is {resistors[0]:.1f} ohm and {resistors[1]:.1f} ohm resistors connected in parallel.")
                return

        

        p_difference = abs(target - parallel[0])
        s_difference = abs(target - series[0])

        if(s_difference < p_difference or s_difference == p_difference):
            # series one is better
            resistors = [series[1], series[2]]
            print(f"The best combination of resistors is {resistors[0]:.1f} ohm and {resistors[1]:.1f} ohm resistors connected in series.")
            return

        if(s_difference > p_difference):
            # parallel one is better
            resistors = [parallel[1], parallel[2]]
            print(f"The best combination of resistors is {resistors[0]:.1f} ohm and {resistors[1]:.1f} ohm resistors connected in parallel.")
            return


main()