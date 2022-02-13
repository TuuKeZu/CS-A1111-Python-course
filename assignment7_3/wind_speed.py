AIR_DENSITY = 1.225 # kg/m^3
AREA = 8659 # m^2
CUT_IN = 3 # m/s
CUT_OUT = 25 # m/s
MAX_POWER = 3450 # kW

def calculate_powers(velocities_list):
    power_list = []
    for velocity in velocities_list:
        if(velocity >= CUT_IN and velocity <= CUT_OUT):
            power = 8/27 * AIR_DENSITY * (velocity ** 3) * AREA
            power_in_KW = power/1000
            power_list.append(power_in_KW)
        else:
            power_list.append(0.0)
    
    return(power_list)

def calculate_capacity_factor(power_list):
    maximium_possible_power = len(power_list) * MAX_POWER
    power = sum(power_list)
    capacity_factor = power / maximium_possible_power

    return capacity_factor


def main():
    file_name = input("Enter the name of the file containing wind velocities.\n")
    try:
        file = open(file_name, "r")

        data = file.readlines()
        del data[0]
        speeds = []

        for i in range(len(data)):
                line = data[i].strip()
                data_array = line.split(',')

                if(len(data_array) == 6):
                    speeds.append(float(data_array[5]))

        power_list = calculate_powers(speeds)
        capacity_factor = calculate_capacity_factor(power_list)
        peak_power = max(power_list)
        power_total = sum(power_list)
        print()
        print(f"The maximum power of the wind turbine was {peak_power:.1f} kW.")
        print(f"The wind turbine generated {power_total:.1f} kWh of electricity.")
        print(f"The capacity factor of the wind turbine was {capacity_factor:.3f}.")





    except OSError:
        print(f"Error while reading the '{file_name}' file. Program ends.")
        return
main()
