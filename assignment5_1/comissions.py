def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")
    LIMIT = 500             # euros
    NORMAL_COMMISSION = 6.5 / 100 # %
    BONUS_COMMISSION = 13.5 / 100   # %

    comission = 0;

    for sale in sales:
        if(sale >= LIMIT):
            comission += sale * BONUS_COMMISSION;
            print(f"{sale * BONUS_COMMISSION:0.2f} eur")
        else:
            comission += sale * NORMAL_COMMISSION;
            print(f"{sale * NORMAL_COMMISSION:0.2f} eur")

    print(f"Total commissions {comission:0.2f} eur.")

    # Implement your own code here that goes through the list of
    # sales and calculates and prints the commissions based on those sales.

    # Write then a command here that prints the total of commissions.

main()