class RestaurantBill:
    FOOD_VAT = 14.0
    DRINK_VAT = 24.0

    def __init__(self, table_number, waitress_name):
        self.__table = table_number
        self.__waitress = waitress_name
        self.__food = []
        self.__drinks = []

    def get_table(self):
        return self.__table

    def get_waitress(self):
        return self.__waitress

    def get_food_prices(self):
        return self.__food

    def get_drink_prices(self):
        return self.__drinks

    def add_to_bill(self, price, is_drink):
        if(not price < 0):
            if(is_drink):
                self.__drinks.append(price)
            else:
                self.__food.append(price)

    def fix_price(self, line, is_drink, new_price):
        # define which list we are modifying
        
        if(is_drink):
            target_list = self.__drinks
        else:
            target_list = self.__food

        if(new_price < 0):
            return False

        # check the validity of line index
        if(line < 1 or line > (len(target_list))):
            return False

        target_value = target_list[line - 1]

        # check if the value should be removed from the list or changed
        if(new_price == 0.0):
            target_list.remove(target_value)
        else:
            target_list[line - 1] = new_price
        
        return True

    def calculate_drink_prices(self):
        total = sum(self.__drinks) # with tax
        tax_free = total / (1 + (self.DRINK_VAT / 100))
        tax = total - tax_free

        return(tax_free, tax, total)

    def calculate_food_prices(self):
        total = sum(self.__food) # with tax
        tax_free = total / (1 + (self.FOOD_VAT / 100))
        tax = total - tax_free

        return(tax_free, tax, total)

    def calculate_total(self):
        return(self.calculate_drink_prices()[2] + self.calculate_food_prices()[2])
    
    def make_bill(self):
        bill = ""
        bill += f"Table: {self.__table}\n"
        bill += f"Waitress: {self.__waitress}\n"
        bill += "FOOD:\n"

        for food in self.__food:
            bill += '{:>16s}\n'.format(f"{food:.2f}")

        bill += "DRINKS:\n"
        
        for drink in self.__drinks:
           bill += '{:>16s}\n'.format(f"{drink:.2f}")

        bill += "------------------------------\n"
        bill += "Total {:>7s}\n".format(f"{self.calculate_total():.2f}")
        bill += "\n"
        bill += "           sales     VAT     total\n"
        bill += "VAT 24 %: {:>7s} {:>7s} {:>7s}\n".format(f"{(self.calculate_drink_prices()[0]):.2f}", f"{(self.calculate_drink_prices()[1]):.2f}", f"{(self.calculate_drink_prices()[2]):.2f}")
        bill += "VAT 14 %: {:>7s} {:>7s} {:>7s}".format(f"{(self.calculate_food_prices()[0]):.2f}", f"{(self.calculate_food_prices()[1]):.2f}", f"{(self.calculate_food_prices()[2]):.2f}")
        return bill

    def __str__(self):
        s = ""
        s += f"Table: {self.__table}\n"
        s += f"Waitress: {self.__waitress}\n"
        s += f"Total sum so far: {self.calculate_total():.2f} eur."

        return s