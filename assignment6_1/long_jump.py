def main():
    results_str = input("Enter the lengths of the jumps (cm) separated by commas.\n")

    if(results_str == ""):
        print("No accepted results.")
        return
    
    results = results_str.split(',')
    # muutetaan kaikki listan arvot kokonaisluvuoksi
    for result in results:
        result = int(result)

    # lajitellaan muuttuja pienimmästä suurimpaan

    results.sort(reverse=True)

    # lopuksi printataan paras hyppy
    print(f"The best result is {results[0]} cm.")




main()