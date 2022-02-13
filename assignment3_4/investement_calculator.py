def main():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year','Month','Start','Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:
    monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1

    # Write your code here

main()