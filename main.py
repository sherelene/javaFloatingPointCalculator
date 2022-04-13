# This function is for the dfa = starting state
# dfa = state (zeroth) of DFA
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


# This function is for the next state after the start state
# dfa = state of DFA
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
# dfa = state of DFA
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


# This function is for the third
# dfa = state of DFA
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


# dfa if number was found after decimal
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


# accept state
def state5(c):
    accept_end = {"f": "f", "F": "F"}
    if c in accept_end:
        dfa = 5
        return dfa, accept_end[c]
    return dfa, 0


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
    if String == "_":
        return False, 0
    elif String == ".":
        return False, 0

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

        # if "_" is found in input string, it is ignored
        if "_" == num:
            continue
            # saves index where e or E is found
        elif "." == num:
            dot_index = cnt
            dot_found = True
            characters.append(num)
        elif "e" == num or "E" == num:
            e_index = cnt
            e_found = True
            characters.append(num)
        elif "+" == num:
            continue
        elif "-" == num:
            minus_found = True
        elif "f" == num or "F" == num:
            continue
        else:
            characters.append(num)
        cnt = cnt + 1

    # accepted states
    if dfa == 6 or dfa == 4 or dfa == 5 or dfa == 2:
        number = get_num(characters, e_index, e_found, dot_index, dot_found, minus_found, minus_index)
        return True, number
    else:
        return False, 0


def get_num(characters, e_index, e_found, dot_index, dot_found, minus_found, minus_index):
    length = len(characters)
    sum = 0
    whole_num = 0
    decimals = 0
    ind = 0

    # if decimal number
    if dot_found:
        before_dot = dot_index - 1  #minus two because starts from 10^0 and not 10^1
        after_dot = -1

        #gets the numbers before the decimals
        for i in range(before_dot, -1, -1):
            whole_num = whole_num + (characters[ind] * 10 ** i)
            ind = ind + 1
            print("whole", whole_num)

        #if theres numbers after the decimals and theres an exponent
        if dot_index != length and e_found:
            for j in range(dot_index + 1, e_index):
                decimals = decimals + characters[j] * 10 ** after_dot  #adds numbers after decimals to whole number
                after_dot = after_dot - 1
                exp_length = (length - e_index) - 2

                #if negative sign found with exponent
                if minus_found:
                    for k in range(e_index + 1, length):
                        power = characters[k] * 10 ** exp_length
                        exp_length = exp_length + 1
                        power = -power
                else:
                    for k in range(e_index + 1, length):
                        power = characters[k] * 10 ** exp_length
                        exp_length = exp_length + 1

        elif dot_index != length:
            for j in range(dot_index+1, length):
                decimals = decimals + characters[j] * 10 ** after_dot
                after_dot = after_dot - 1
                print(characters[j] * 10 ** after_dot)
                print("dd", decimals)
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
            power = characters[j] * 10 ** exp_length
            exp_length = exp_length + 1
        sum = (whole_num + decimals) * 10 ** power

    else:
        for i in range(length-1, -1, -1):
            sum = sum + characters[ind] * 10 ** i
            ind = ind + 1

    return sum


def main(input_string):
    accepted, number = isAccepted(input_string)
    if accepted:
        print(number)
    else:
        print("reject")

def sanity_check():
    test_num = ['', '123', '123f', '123e', '123e1', '123e1f', '+123f', '-123f',
                '123.', '.', '123..2', '123.2.e1', '_', '_1__2.', '1__2.', '1__2_.',
                '123._2', '123.2_e1', '123.2_e_1', '123.3e1', '.123e4', '5.432e-2']

    for element in test_num:
        print(element)
        main(element)

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





