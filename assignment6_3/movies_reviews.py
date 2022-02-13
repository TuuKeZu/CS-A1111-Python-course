MOVIE_DATABASE = {}
VALID_INPUTS = [1, 2, 3, 4, 5]


def ask_user_input():
    type = int(input("Choose 1-5.\n1: Add a new movie and rating.\n2: Change the rating of the movie.\n3: Print all movies and their ratings.\n4: Find all movies with a specific rating.\n5: Exit.\n"))

    while(type not in VALID_INPUTS): 
        print("\nYou chose an invalid number.\n")
        type = int(input("Choose 1-5.\n1: Add a new movie and rating.\n2: Change the rating of the movie.\n3: Print all movies and their ratings.\n4: Find all movies with a specific rating.\n5: Exit.\n"))
    else:
        return type


def add_new_movie_and_rating(dictionary, movie, rating):
    # tarkistetaan onko elokuva jo avaimena listassa
    if(movie in dictionary.keys()):
        return False;

    dictionary[movie] = rating;
    return True;

def change_rating(dictionary, movie, rating):
    if(movie not in dictionary.keys()):
        return False;
    else:
        dictionary[movie] = rating;

    return True;

def print_all_movies(dictionary):
    sorted_list = sorted(dictionary.keys())
    for movie in sorted_list:
        print(f"{movie} {dictionary[movie]}");
    return

def find_movies_with_rating(dictionary, rating):
    found_movies = []

    for movie in dictionary:
        if(dictionary[movie] == rating):
            found_movies.append(movie)

    return found_movies


def main():
    print("Welcome to the database of the movie ratings.\n")
    response = ask_user_input()

    while(response != 5):

        # oispa se vitun switch

        if(response == 1):
            name = input("\nEnter the movie.\n")
            rating = input("Enter the rating (4-10).\n")
            status = add_new_movie_and_rating(MOVIE_DATABASE, name, rating)

            if(status == True):
                print(f"{name} has been added into the database.\n")
            if(status == False):
                print(f"{name} is already in the database. Choose 2 if you want to change the rating of the movie.\n")

        elif(response == 2):
            name = input("\nEnter the movie.\n")
            rating = input("Enter the new rating (4-10).\n")
            status = change_rating(MOVIE_DATABASE, name, rating)

            if(status == True):
                print(f"The rating of {name} has been changed.\n")
            if(status == False):
                print(f"{name} is not in the database. Choose 1 if you want to add the movie.\n")

        elif(response == 3):
            print("\nThe movies in the database:")
            print_all_movies(MOVIE_DATABASE)
            print()
        elif(response == 4):
            rating = input("\nEnter the rating.\n")
            result = find_movies_with_rating(MOVIE_DATABASE, rating)

            if(len(result) == 0):
                print(f"There are no movies with rating {rating} in the database.\n")
            else:
                for movie in result:
                    print(movie)
                print()


        response = ask_user_input()


    return

main()
