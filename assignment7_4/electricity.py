SIZE_LESS_THAN_110 = 15 # %
SIZE_OVER_110 = 5 #%


def calculate_consumption(size, residents):
    power_consuption = 2206 # kWh;
    size_increase = size - 30
    if(size > 30 and size <= 110):
        size_increase_k = -(-size_increase//10)
        print(size_increase_k)
        power_consuption += size_increase_k * (SIZE_LESS_THAN_110 / 100)

    elif(size > 110):
        size_increase_k = -(-size_increase//10)
        power_consuption += size_increase_k * (SIZE_OVER_110 / 100)

    if(residents <= 3):
        power_consuption += power_consuption * 0.12
    else:
        power_consuption += power_consuption * 0.07


    return power_consuption



print(calculate_consumption(45, 2))