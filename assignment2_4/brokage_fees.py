def Main():
    trade_value = 0.0;
    fees = 0.0;

    print("Enter the values of the trades in separated lines. Stop with a negative value.")

    while(trade_value >= 0):
        value = float(input("Enter next value of the trade." + "\n"))
        trade_value = value

        if(trade_value < 0):
            print("The brokerage fees are "+str(fees)+" eur.")
            return


        if(value < 800):
            fees += (trade_value * 0.01)
        if(value >= 800):
            if(value * 0.002 < 8):
                fees += 8
            
            if(value * 0.002 >= 8):
                fees += (trade_value * 0.002)
    

Main()

            