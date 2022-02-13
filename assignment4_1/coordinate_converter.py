# Implement the function convert_DMS_to_decimal_degrees here.
DMS = [0.0] * 3;

def convert_DMS_to_decimal_degrees():
    DMS[0] = float(input("Enter the degrees:\n"));
    DMS[1] = float(input("Enter the minutes:\n"));
    DMS[2] = float(input("Enter the seconds:\n"));
    decimal_degrees = DMS[0] + (DMS[1] / 60) + (DMS[2] / 3600)
    print(f"In decimal degrees: {decimal_degrees:2.6f}")

def main():
    print("Choose an action:")
    print("1. Convert DMS to decimal degrees.")
    print("2. End.")
    choice = int(input())
    while choice != 2:
        print()
        print("LATITUDE:")
        convert_DMS_to_decimal_degrees()
        print("LONGITUDE:")
        convert_DMS_to_decimal_degrees()
        print()
        print("Choose an action:")
        print("1. Convert DMS to decimal degrees.")
        print("2. End.")
        choice = int(input())
        
    print("\nProgram ends.")

main()