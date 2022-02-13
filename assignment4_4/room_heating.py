AIR_DENSITY = 1.225 # kg/m3
SPECIFIC_HEAT_CAPACITY_AIR = 1012 # J/(kg*celcius)
COMPUTER_HEATING_RATIO = 0.92
LIGHTS_HEATING_RATIO = 0.90
OVEN_HEATING_RATIO = 0.95
WASHING_MACHINE_HEATING_RATIO = 0.80
ERROR_WITH_WARMING = -99
KWH_PRICE = 9.89 # cents/kWh
AVAILABLE_DEVICE_TYPES = ["computer", "lights", "oven", "washing machine"]

def calculate_warming(power, time, device_type, room_size):

    if(time < 0 or power < 0):
        return(-99)

    if device_type not in AVAILABLE_DEVICE_TYPES:
        return(-99)
    
    ratio = 0;

    # oispa switch case...
    if(device_type == AVAILABLE_DEVICE_TYPES[0]):
        ratio = COMPUTER_HEATING_RATIO;
    elif(device_type == AVAILABLE_DEVICE_TYPES[1]):
        ratio = LIGHTS_HEATING_RATIO;
    elif(device_type == AVAILABLE_DEVICE_TYPES[2]):
        ratio = OVEN_HEATING_RATIO;
    elif(device_type == AVAILABLE_DEVICE_TYPES[3]):
        ratio = WASHING_MACHINE_HEATING_RATIO;



    temp_rise = ratio * power * (time*60) / (SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size);
    return temp_rise


def calculate_costs(power, time):
    if(power < 0 or time < 0):
        return(-99)
    
    power_usage = (power/1000) * (time/60)
    costs = KWH_PRICE * power_usage
    return(costs)

def main():
    total_temp = 0;
    total_cost = 0;

    room_size = float(input("Enter the size of the room (m3).\n"))
    answer = "";
    while(answer != "no"):
        type = input("Enter the device type (computer, lights, oven or washing machine).\n")
        power = float(input("Enter the power of the device (W).\n"))
        time = float(input("Enter time of use (min).\n"))
        temp = calculate_warming(power, time, type, room_size)
        cost = calculate_costs(power, time)

        if(temp != -99):
            total_temp += temp;
        else:
            print("Invalid input.")

        if(cost != -99):
            total_cost += cost;
        else:
            print("Invalid input.")

        answer = input("Do you want to enter another device (yes or no)?\n")

        
    else:
        print(f"The electric devices heat the room by {total_temp:.2f} degrees and it costs {total_cost:.2f} cents.")
        return

        


main()