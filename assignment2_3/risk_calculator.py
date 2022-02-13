
def CalcRisk(age, weight, height, genes):
    risk_index = 0;
    läheis_pisteet = 0;
    ikä_pisteet = 0;
    paino = 0;

    weight_index = weight / ((height / 100) ** 2)

    #checking the genes
    if(genes == "yes"):
        risk_index += 5
        läheis_pisteet = 5;

    #check for the weight index

    if(weight_index >= 25):
        if(weight_index <= 30):
            risk_index += 1
            paino = 1;
        else:
            risk_index += 2
            paino = 2;

    #check for the age

    if(age >= 45 and age <= 54):
        risk_index += 2
        ikä_pisteet = 2;

    if(age >= 55 and age <= 64):
        risk_index += 3
        ikä_pisteet = 3;

    if(age > 64):
        risk_index += 4
        ikä_pisteet = 4;

    #calculate the conclusion

    print(ikä_pisteet, " : ", paino, " : ", läheis_pisteet);

    if(risk_index == 0):
        return "low"

    if(risk_index >= 1 and risk_index < 5):
        return "moderate"

    if(risk_index >= 5):
        return "high"

def Main():
    age = input("Enter your age." + "\n")
    weight = input("Enter your weight in kilograms." + "\n")
    height = input("Enter your height in centimeters." + "\n")
    genes = input("Has your parent or sibling been diagnosed with type 1 or type 2 diabetes? Enter yes or no." + "\n")
    
    print("You have a "+CalcRisk(int(age), float(weight),float(height), genes)+" risk of getting type 2 diabetes.")
    
Main()
    
