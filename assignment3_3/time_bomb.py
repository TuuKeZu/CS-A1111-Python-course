import random


def main():
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    MIN_GUESSES = 7
    MAX_GUESSES = 20

    # Generate the random number and the number of guesses
    original_seed = int(input("Enter a seed:\n"))
    random.seed(original_seed)

    right_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses_left = random.randint(MIN_GUESSES, MAX_GUESSES)

    guess = int(input("Enter your guess:" + "\n"));

    while(guess != right_number):
        guesses_left -= 1;

        if(guesses_left == 0):
            print("KABOOM!");
            print("You didn't find the right number in time and the bomb exploded.");
            print("The right number was " + str(right_number) + ".");
            return;

        while(guess > MAX_NUMBER or guess < MIN_NUMBER):
            print("The number is between 0 and 1000.");
            guess = int(input("Enter the next guess:" + "\n"));
            guesses_left -= 1;

            if(guesses_left == 0):
                print("KABOOM!");
                print("You didn't find the right number in time and the bomb exploded.");
                print("The right number was " + str(right_number) + ".");
                return;


        if(guess < right_number):
            print("The number is bigger.");
            
        if(guess > right_number):
            print("The number is smaller.");

        if(guesses_left == 1):
            print("You have 1 guess left!");
        guess = int(input("Enter the next guess:" + "\n"));
        
    else:
        print("You found the right number in time!");
        print("The right number was " + str(right_number) + ".");
        return;



main()