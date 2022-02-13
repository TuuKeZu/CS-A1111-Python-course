VOCALS = ['a', 'e', 'i', 'u', 'o', 'y']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y']


def generate_nickname(name):
    name = name.lower()

    vocals = []
    consonants = []
    name_lenght = 0
    result = ""
    for letter in name:
        if(letter in VOCALS):
            vocals.append(letter)
        elif(letter in CONSONANTS):
            consonants.append(letter)

    if(len(vocals) >= 3 and len(consonants) >= 3):
        # the lenght of the name will be 6 chars
        name_lenght = 6
        
    elif(len(vocals) >= 2 and len(consonants) >= 2):
        # the lenght of the name will be 4 chars
        name_lenght = 4
        
    else:
        # name cannot be generated
        return -1
    
    vocal_index = len(vocals) - 1;
    consonant_index = len(consonants) - 1;
    for i in range(name_lenght):

        # jos nykyinen indeksi on parillinen (vokaali)
        if(i == 0):
            result += consonants[consonant_index].upper()
            consonant_index -= 1
        else:
            if(i % 2 == 1):
                result += vocals[vocal_index]
                vocal_index -= 1
            else:
                result += consonants[consonant_index]
                consonant_index -= 1

    if(result.lower() != name.lower()):
        return result
    else:
        return -1


def main():
    name = input("Enter your name.\n")
    nick = generate_nickname(name)

    if(nick != -1):
        print("\nYour nickname: "+nick)
    else:
        print("\nNot able to generate a nickname.")


main()