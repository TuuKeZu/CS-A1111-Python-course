def CalcDifference(uses_per_weeks, one_time_use_prize, monthly_lens_prize, lens_solution_prize):
    monthly_uses = uses_per_weeks * 4;
    prize_per_switch = lens_solution_prize * 0.05;

    monthly_prize = (prize_per_switch * monthly_uses) + monthly_lens_prize
    daily_prize = one_time_use_prize * monthly_uses

    if(monthly_prize < daily_prize):
        if((monthly_prize < daily_prize) <= 5):
            print("you should buy montly lenses")
            print("They cost " + str(monthly_prize) + " per month, which is " + str(daily_prize - monthly_prize) + " cheaper than daily lens")
        else:
            print("you should buy daily lenses")
            print("They cost " + str(daily_prize) + " per month, which is " + str(monthly_prize - daily_prize) + " cheaper than monthly lens")
    else:
        print("You should buy daily lenses.")
        print("They cost " + str(daily_prize) + " per month, which is " + str(monthly_prize - daily_prize) + " cheaper than monthly lens")
    
def Main():
    uses_per_week = input("How many days a week do you use contact lenses?" + "\n")
    daily_lens = input("How much do the daily lenses cost per pair?" + "\n")
    monthly_lens = input("How much do the monthly lenses cost per pair?" + "\n")
    lens_solution = input("How much does the contact lens solution cost? (euros per 100 ml)" + "\n")

    CalcDifference(int(uses_per_week), float(daily_lens), float(monthly_lens), float(lens_solution))

Main()