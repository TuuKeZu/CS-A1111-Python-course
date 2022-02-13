INSURANCE_CEILING = 2500.0;
CURRENT_YEAR = 2021;
MAX_AGE_REDUCTION = 0.70;
DEDUCTIBLE = 150;


def main():
    prize = float(input("Enter the purchase price of your computer, smart watch or phone." + "\n"))
    # tarkista onko tuotteen hinta positiivinen
    while(prize <= 0):
        prize = float(input("Incorrect value. Enter again the value of your device." + "\n"))

    if(prize <= DEDUCTIBLE):
        print("The value of your device is less than or equal to the deductible.")
        print("The compensation is 0.0 eur.");
        return


    year_of_purchace = int(input("Enter the year of the purchase." + "\n"))
    # tarkista onko ostovuosi pienempi tai sama kuin nykyinen
    while(year_of_purchace > CURRENT_YEAR):
        year_of_purchace = int(input("The year is not valid. Enter again the year of the purchase." + "\n"))

    compensation = 0;
    age_reduction_percent = (CURRENT_YEAR - year_of_purchace)*(0.25);

    # tarkistetaan onko laitteen hinta vähemmän ta yhtäsuuri kuin omavastuu

    
    # tarkistetaan onko ikä-vähennys suurempi kuin yläraja => jos on niin asetetaan se ylärajaan
    if(age_reduction_percent > 0.70):
        age_reduction_percent = 0.70

    age_reduction = age_reduction_percent*prize;

    compensation = (prize - (DEDUCTIBLE + age_reduction))

    # tarkistetaan onko korvaus suurempi kuin yläraja => jos on, asetetaan se yläräjaan
    if(compensation > INSURANCE_CEILING):
        compensation = INSURANCE_CEILING;

    #tarkistetaan onko korvaus negatiivinen => jos on, asetetaan sen arvo 0€

    if(compensation < 0):
        compensation = 0.0

    

    print("The compensation is", compensation, "eur.");

main()