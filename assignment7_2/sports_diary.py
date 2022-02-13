def read_sport_from_file(file_name, sports):
    try:

        file = open(file_name)
        data_list = []

        print("Day        Time")

        for line in file:
            line = line.rstrip()
            data = line.split(',')

            if(data[1] == sports):
                data_list.append(data)
        file.close()

        if(len(data_list) == 0):
            print(f"The sport '{sports}' was not found in the file.")
            return
        else:
            total_time = 0;
            total_count = 0;
            for data in data_list:
                date = data[0]
                time = int(data[2])
                print(f"{date}   {time} min")

                total_time += time
                total_count += 1

            print("-" * 31)
            f_total_time = convert_mins_to_hours_and_minutes(total_time)
            print(f"Total exercise time: {f_total_time[0]} h {f_total_time[1]} min")
            print(f"Number of exercise days: {total_count}")


    except OSError:
        print(f"Error in reading the file '{file_name}'. Program ends.")
        return
    except ValueError:
        print(f"Incorrect time in the file '{file_name}'. Program ends.")
        return

def validate_file(file_name):
    try:
        file = open(file_name)
        file.close()
        return 200
    except OSError:
        print(f"Error in reading the file '{file_name}'. Program ends.")
        return 400

def convert_mins_to_hours_and_minutes(mins): # palauttaa minuutit tunteina listana muodossa: [tunnit, minuutit]
    minutes = mins
    hours = 0;

    while((minutes - 60) >= 0):
        minutes -= 60
        hours += 1
    else:
        return([hours, minutes])

def main():
    file_name = input("Enter the name of the file containing your exercise diary:\n")

    status = validate_file(file_name)

    if(status == 200):
        sport_name = input("What sport are you interested in?\n")
        read_sport_from_file(file_name, sport_name)
    else:
        return


main()


