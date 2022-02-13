def find_median(number1, number2, number3):
    sorted_list = [number1, number2, number3];
    sorted_list.sort()
    return sorted_list[1];

def median_filter(signal):
    result = [];
    index = 0;

    for s in signal:
        if(index != 0 and index != (len(signal) - 1)):
            result.append(find_median(signal[index -1], s, signal[index + 1]))
        else:
            result.append(s)
        
        index += 1;
    return result;


def main():
    signal = []

    data = input("Enter the data points of the signal. Stop with empty line.\n")

    while(data != ''):
        signal.append(float(data))
        data = input('')

    else:
        print(f"The original signal is {signal}")
        print(f"The median filtered signal is {median_filter(signal)}")
        return;


main()