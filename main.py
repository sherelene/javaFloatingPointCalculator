
# This function is for the dfa = starting state
def start(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    if c in accept_nums:
        dfa = 1
        return dfa, accept_nums[c]
    elif c == ".":
        dfa = 4
        return dfa, '.'
    # -1 is used to check for any
    # invalid symbol
    else:
        dfa = -1
    return dfa, 0


# This function is for the next state after the start state if start state was a 0-9
# Accepts input 0-9 returns to itself
# Accepts e, E next state 3
# Accepts f, f next state 5 -> accept/end state
def state1(c):
    dot = "."
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9, "_": "_"}
    accept_chars = {"e": "E"}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 1
        return dfa, accept_nums[c]
    elif c == dot:
        dfa = 2
        return dfa, dot
    elif c in accept_chars:
        dfa = 3
        return dfa, accept_chars[c]
    elif c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    else:
        dfa = -1
    return dfa, 0


# This function next state if previous state was a "."
# Accepts input 0-9 returns to itself
# Accepts e, E next state 3
# Accepts f, f next state 5 -> accept/end state
def state2(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_chars = {"e": "E"}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 2
        return dfa, accept_nums[c]
    elif c in accept_chars:
        dfa = 3
        return dfa, accept_chars[c]
    elif c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    else:
        dfa = -1
    return dfa, 0


# This function is for after an e, E
# Required input (0-9, +,or -) next state 6
def state3(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_operators = {"+": "+", "-": "-"}
    if c in accept_operators:
        dfa = 6
        return dfa, accept_operators[c]
    elif c in accept_nums:
        dfa = 6
        return dfa, accept_nums[c]
    else:
        dfa = -1
    return dfa, 0


# This function is for the next state after the start state if start state was a .
# Accepts input 0-9 next state 2
# Accepts f, f next state 5 -> end state
def state4(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 2
        return dfa, accept_nums[c]
    elif c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    else:
        dfa = -1
    return dfa, 0


# Accepts only f, F- accept/end state
def state5(c):
    accept_end = {"f": "f", "F": "F"}
    if c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    else:
        dfa = -1
    return dfa, 0


# This function is only called if there is an exponent and after state 3
# Accepts input 0-9 returns to itself
# Accepts f, f next state 5 -> end state
def state6(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 6
        return dfa, accept_nums[c]
    elif c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    else:
        dfa = -1
    return dfa, 0


def isAccepted(String):
    # store length of Stringing
    length = len(String)
    # initialize variables and array for converting to float
    characters = []
    cnt = 0
    e_found = False
    e_index = 0
    dot_index = 0
    dot_found = False
    minus_index = 0
    minus_found = False

    # dfa tells the number associated
    # with the present dfa = state
    dfa = 0

    # Some fail safes if input is a _ or . only
    if String == "_":
        return False, 0
    elif String == ".":
        return False, 0

    # DFA to determine if input is acceptable
    for i in range(length):
        if dfa == 0:
            dfa, num = start(String[i])
        elif dfa == 1:
            dfa, num = state1(String[i])
        elif dfa == 2:
            dfa, num = state2(String[i])
        elif dfa == 3:
            dfa, num = state3(String[i])
        elif dfa == 4:
            dfa, num = state4(String[i])
        elif dfa == 5:
            dfa, num = state5(String[i])
        elif dfa == 6:
            dfa, num = state6(String[i])
        else:
            return False, 0

        # if "_" is the current character, it is ignored
        if "_" == num:
            continue
        # saves index where . is found and adds to character array
        elif "." == num:
            dot_index = cnt
            dot_found = True
            characters.append(num)
        # saves index where e or E is found and adds to character array
        elif "e" == num or "E" == num:
            e_index = cnt
            e_found = True
            characters.append(num)
        # if "_" is the current character, it is ignored
        elif "+" == num:
            continue
        # if negative it means it is an accepted negative which means it is a negative
        # found after the exponent. Store minus_found as True
        elif "-" == num:
            minus_found = True
        # if "f" or "F" is the current character, it is ignored
        elif "f" == num or "F" == num:
            continue
        else:  # numbers are added to character array to be converted to a float
            characters.append(num)

        # keeps track of character array indexes
        cnt = cnt + 1

    # accepted states of the dfa
    if dfa == 6 or dfa == 4 or dfa == 5 or dfa == 2:
        # function to take character array and transform into a float
        number = get_num(characters, e_index, e_found, dot_index, dot_found, minus_found)
        return True, number
    else:
        return False, 0


def get_num(characters, e_index, e_found, dot_index, dot_found, minus_found):
    # initialize variables for help converting to float
    length = len(characters)
    sum = 0
    whole_num = 0
    decimals = 0
    ind = 0
    power = 0

    # if input was a decimal number
    if dot_found:
        # index for adding numbers before and after the dot
        before_dot = dot_index - 1
        after_dot = -1

        # gets the numbers before the decimals
        for i in range(before_dot, -1, -1):
            whole_num = whole_num + (characters[ind] * 10 ** i)
            ind = ind + 1

        #if theres numbers after the decimals and theres an exponent
        if dot_index != length and e_found:
            # starting from after the dot until the exponent
            for j in range(dot_index + 1, e_index):
                # after_dot is 10 ^-1
                # so if the number is .123, it will be 1 x 10 ^ -1 = .1
                decimals = decimals + characters[j] * 10 ** after_dot
                # then it will be after_dot = -1 - 1 =  2 x 10 ^-2 = . 02
                after_dot = after_dot - 1

                # since exponent IS found, exp_length is length of exponent eg. e10 is length 2
                # eg 123.45e2 is (8(length)- 6(e_index)) - 2 = 0 therefore exp_length has only 10^0
                # eg 123.45e25 is (9(length)- 6(e_index)) - 2 = 1 therefore exp_length has 10^0 and 10^1
                exp_length = (length - e_index) - 2

                #if negative sign found with exponent
                if minus_found:
                    for k in range(e_index + 1, length):
                        power = power +  characters[k] * 10 ** exp_length
                        exp_length = exp_length + 1
                        power = -power
                else:
                    for k in range(e_index + 1, length):
                        power = power + characters[k] * 10 ** exp_length
                        exp_length = exp_length + 1

        elif dot_index != length:
            for j in range(dot_index+1, length):
                decimals = decimals + characters[j] * 10 ** after_dot
                after_dot = after_dot - 1
            sum = whole_num + decimals
        else:
            sum = whole_num + decimals

        if e_found:
            sum = (whole_num + decimals) * 10 ** power
        else:
            sum = whole_num + decimals

    elif e_found:
        ind = 0
        exp_length = (length - e_index) - 2
        for i in range(e_index-1, -1, -1):
            decimals = decimals + characters[ind] * 10 ** i
            ind = ind + 1
        for j in range(e_index+1, length):
            power = power + characters[j] * 10 ** exp_length
            exp_length = exp_length + 1
        sum = (whole_num + decimals) * 10 ** power

    else:
        for i in range(length-1, -1, -1):
            sum = sum + characters[ind] * 10 ** i
            ind = ind + 1

    return sum


def sanity_check():
    test_num = ['', '123', '123f', '123e', '123e1', '123e1f', '+123f', '-123f',
                '123.', '.', '123..2', '123.2.e1', '_', '_1__2.', '1__2.', '1__2_.',
                '123._2', '123.2_e1', '123.2_e_1', '123.3e1', '.123e4', '5.432e-2', '1111111111.0e-11']

    for element in test_num:
        print(element)
        main(element)


def main(input_string):
    accepted, number = isAccepted(input_string)
    if accepted:
        print(number)
    else:
        print("reject")


if __name__ == '__main__':
    again = True

    # Function to check code and make sure it works fine
    sanity_check()

    print("enter 'q' or 'quit' to exit")
    while again:
          user_input = input('Please enter your floating point literal: ')
          main(user_input)
          if user_input == 'q' or user_input == "quit":
              again = False





