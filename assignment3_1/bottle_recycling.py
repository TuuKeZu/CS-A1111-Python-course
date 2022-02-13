def main():
    CAN = 0
    GLASS_BOTTLE = 1
    PLASTIC_SMALL = 2
    PLASTIC_NORMAL = 3
    PLASTIC_BIG = 4
    NO_DEPOSIT_BOTTLE = 5
    CAN_DEPOSIT = 15            # cents
    GLASS_BOTTLE_DEPOSIT = 10   # cents
    PLASTIC_SMALL_DEPOSIT = 10  # cents
    PLASTIC_NORMAL_DEPOSIT = 20 # cents
    PLASTIC_BIG_DEPOSIT = 40    # cents

    VALID_TYPES = [CAN, GLASS_BOTTLE, PLASTIC_SMALL, PLASTIC_NORMAL, PLASTIC_BIG, NO_DEPOSIT_BOTTLE]

    print("Welcome to the bottle recycling.")
    print("Bottle types with the corresponding numbers:")
    print("Can: 0")
    print("Glass bottle: 1")
    print("Plastic bottle (0.33l): 2")
    print("Plastic bottle(0.5l): 3")
    print("Plastic bottle (1.5l): 4")
    print("No deposit bottle: 5")
    bottle = float(input("Enter the type of the first bottle. Stop with a negative number:\n"))

    bounty_from_deposit = 0; #cents

    while(bottle >= 0):
        # oispa switch statement...

        # tarkistetaan onko pullo oikeanlainen:
        bottle_is_valid = True;

        if bottle not in VALID_TYPES:
            print("Unknown bottle type.");
            bottle_is_valid = False;

        # jos pullo on oikeanalinen, tarkista sen pantti ja lisää se kokonaissummaan
        if(bottle_is_valid):

            if(bottle == CAN):
                bounty_from_deposit += CAN_DEPOSIT

            elif(bottle == GLASS_BOTTLE):
                bounty_from_deposit += GLASS_BOTTLE_DEPOSIT

            elif(bottle == PLASTIC_SMALL):
                bounty_from_deposit += PLASTIC_SMALL_DEPOSIT

            elif(bottle == PLASTIC_NORMAL):
                bounty_from_deposit += PLASTIC_NORMAL_DEPOSIT

            elif(bottle == PLASTIC_BIG):
                bounty_from_deposit += PLASTIC_BIG_DEPOSIT

            elif(bottle == NO_DEPOSIT_BOTTLE):
                # pullolla ei ole panttia, älä tee mitään
                bounty_from_deposit += 0

        bottle = float(input("Enter the type of the next bottle. Stop with a negative number:\n"))
    else:
        print("You got", CentsToEuro(bounty_from_deposit)[0], "euros and", CentsToEuro(bounty_from_deposit)[1], "cents from the bottles.");


    # Implement your code here.
    # int(input("Enter the type of the first bottle. Stop with a negative number:\n"))

# muunna sentit euroiksi ja senteiksi

def CentsToEuro(cents): # palauttaa arrayn [0, eurot], [1, sentit]
    F_eur_string = f"{cents/100:3.2f}";
    F_eur_string = F_eur_string.split('.', 1);
    
    total_eurs = int(F_eur_string[0]);
    total_cents = int(F_eur_string[1]);
    return([total_eurs, total_cents]);

main()