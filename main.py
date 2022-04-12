
def main(input_string):
    # initializing variables to determine state
    index = 0
    character_count = 0
    # initializing strings to store characters
    whole_number = ''
    power = ''

    # checks if the last character in input string is an F or f
    if input_string[-1] == 'f' or input_string[-1] == 'F':
        input_string = input_string[:-1]  # deletes f or f from input string if found in last character

    # checks every character in input_string one by one
    for i in range(len(input_string)):
        # if "_" is found in input string, it is ignored
        if "_" == input_string[i]:
            continue
        # saves index where e or E is found
        elif "e" == input_string[i] or "E" == input_string[i]:
            index = i
            # puts every number after e into a string to be converted into a float later
            for j in range(index + 1, len(input_string)):
                if "_" == input_string[j]:  # if "_" is found in input string, it is ignored
                    continue
                else:
                    power = power + input_string[j]
            break  # breaks for loop so any number after e won't be included in the whole_number string
        else:
            whole_number = whole_number + input_string[i]

        character_count = character_count + 1
    # if index != character_count then an e was in input_string and needs to be multiplied
    if index >= character_count:
        # takes all characters after the index where e was found and converts list to a string to a float
        #multiplier = float(power)
        multiplier = convert(power)
        # takes all characters before the index where e was found and converts list to a string to a float
        #number = float(whole_number)
        number = convert(whole_number)
        num = number * 10 ** multiplier
        is_int(num)
    else:
        is_int(float(whole_number))

    # asks user if they would like to input another string
    retry = input("Would you like to try again? y or n: ")
    if retry == 'Y' or retry == 'y' or retry == 'Yes' or retry == 'yes':
        return True
    else:
        return False


# function to print a whole number or a decimal point
def is_int(x):
    if x % 1 == 0:
        print(int(x))
    else:
        print(x)


def convert(characters):
    # Initialize a variable
    num = 0
    n = len(characters)

    # Iterate till length of the string
    for i in characters:
        # Subtract 48 from the current digit
        num = num * 10 + (ord(i) - 48)

        # return the answer
    return num


if __name__ == '__main__':
    again = True
    while again:
        user_input = input('Please enter your floating point literal: ')
        again = main(user_input)

