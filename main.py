def try_again():
    # asks user if they would like to input another string
    retry = input("Would you like to try again? y or n: ")
    if retry == 'Y' or retry == 'y' or retry == 'Yes' or retry == 'yes':
        return True
    else:
        return False


# Python3 program to implement DFS that accepts
# all Stringing which follow the language
# L = {a ^ n b ^ m (n)mod 2 = 0, m>= 1 }

# This function is for the dfa = starting state
# dfa = state (zeroth) of DFA
def start(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9, "_": "_"}
    if c in accept_nums:
        dfa = 1
    elif c == ".":
        dfa = 4
    # -1 is used to check for any
    # invalid symbol
    else:
        dfa = -1
    return dfa


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
    elif c == dot:
        dfa = 4
    elif c in accept_chars:
        dfa = 3
    elif c in accept_end:
        dfa = 5
    else:
        dfa = -1
    return dfa


# This function next state if previous state was a "."
# dfa = state of DFA
def state2(c):

    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_chars = {"e": "E"}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 2
    elif c in accept_chars:
        dfa = 3
    elif c in accept_end:
        dfa = 5
    else:
        dfa = -1
    return dfa



# This function is for the third
# dfa = state of DFA
def state3(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_operators = {"+": "+", "-": "-"}
    if c in accept_operators:
        dfa = 4
    elif c in accept_nums:
        dfa = 5
    else:
        dfa = -1
    return dfa


# dfa if number was found after decimal
def state4(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 2
    elif c in accept_end:
        dfa = 5
    else:
        dfa = -1
    return dfa


def state6(c):
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9}
    accept_end = {"f": "f", "F": "F"}
    if c in accept_nums:
        dfa = 6
    elif c in accept_end:
        dfa = 5
    else:
        dfa = -1
    return dfa


# accept state
def state5(c):
    accept_end = {"f": "f", "F": "F"}
    if c in accept_end:
        dfa = 5
    return dfa


def isAccepted(String):
    # store length of Stringing
    l = len(String)

    # dfa tells the number associated
    # with the present dfa = state
    dfa = 0
    if String[0] == "_":
        return False
    elif String[0] == "." and l == 1:
        return False

    for i in range(l):
        if dfa == 0:
            dfa = start(String[i])

        elif dfa == 1:
            dfa = state1(String[i])

        elif dfa == 2:
            dfa = state2(String[i])

        elif dfa == 3:
            dfa = state3(String[i])

        elif dfa == 4:
            dfa = state4(String[i])

        elif dfa == 5:
            dfa = state5(String[i])

        elif dfa == 6:
            dfa = state6(String[i])

        else:
            return 0

    if dfa == 6 or dfa == 4 or dfa == 5:
        return True
    else:
        return False



def main(input_string):

    if isAccepted(input_string):
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")


if __name__ == '__main__':
    again = True
    print("enter 'q' or 'quit' to exit")
    while again:
        user_input = input('Please enter your floating point literal: ')
        main(user_input)
        if user_input == 'q' or user_input == "quit":
            again = False
