class RentApartment:
    
    RENTAL_SERVICE_FEE = 100 # eur per month
    STUDIO_SIZE_LIMIT = 32 # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45 # m2
    STUDIO_PRICE_LEVEL = 25 # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20 # eur/m2
    LARGE_PRICE_LEVEL = 18 # eur/m2
    TRANSFER_TAX = 0.02

    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price):
        self.__address = address
        self.__rent = rent
        self.__size = size
        self.__free_of_debt_price = free_of_debt_price
        self.__maintenance_charge = maintenance_charge
        self.__renovation_costs = 0
        self.__rental_service = False

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if(self.__rental_service):
            self.__rental_service = False
            return False
        else:
            self.__rental_service = True
            return True

    def increase_rent(self, new_rent):
        if(self.__rent < new_rent):
            self.__rent = new_rent
            return True
        else:
            return False

    def add_renovation_costs(self, costs):
        self.__renovation_costs += costs

    def calculate_square_meter_rent(self):
        return self.__rent / self.__size

    def calculate_rental_income(self):
        extra_costs = 0

        if(self.__rental_service):
            extra_costs = self.RENTAL_SERVICE_FEE

        income = (self.__rent - (self.__maintenance_charge + extra_costs)) * 12 / (self.__free_of_debt_price + (self.__free_of_debt_price * self.TRANSFER_TAX) + self.get_renovation_costs()) * 100
        # (kuukauden_vuokratulot - kuukauden_kustannukset) * 12 / (velaton_hinta + varainsiirtovero + remonttikustannukset) * 100.
        return income

    def compare_rental_incomes(self, other):
        rental_income = self.calculate_rental_income()
        other_rental_income = other.calculate_rental_income()
        
        if(rental_income == other_rental_income):
            return 0
        elif(rental_income > other_rental_income):
            return 1
        elif(rental_income < other_rental_income):
            return -1

    def calculate_return_on_equity(self, down_payment, loan_interest):
        extra_costs = 0

        if(self.__rental_service):
            extra_costs = self.RENTAL_SERVICE_FEE

        equity = (self.__rent - (self.__maintenance_charge + extra_costs) - loan_interest) * 12 / down_payment * 100
        return equity

    def check_price_level(self):
        size = self.__size
        if(size < 32 and self.calculate_square_meter_rent() >= 25):
            return True

        if(size >= 32 and size < 45 and self.calculate_square_meter_rent() >= 20):
            return True
        
        if(size >= 45 and self.calculate_square_meter_rent() >= 18):
            return True

        return False

    def __str__(self):
        result = ""

        result += "Address: " + str(self.get_address()) + "\n"
        result += "Maintenance charge: " + str(self.get_maintenance_charge()) + " eur \n"
        result += "Size: " + str(self.get_size()) + " m2 \n"
        result += "Rent: " + str(self.get_rent()) + " eur\n"
        if(self.__rental_service):
            result += "Rental service: in use"
        else:
            result += "Rental service: not in use"

        return result

            


        
