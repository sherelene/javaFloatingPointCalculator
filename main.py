def try_again():
    # asks user if they would like to input another string
    retry = input("Would you like to try again? y or n: ")
    if retry == 'Y' or retry == 'y' or retry == 'Yes' or retry == 'yes':
        return True
    else:
        return False

def main(input_string):
    # initializing strings to store characters
    whole_number = ''
    decimal_nums = ''
    power = ''
    num = [len(input_string)]
    # initializing variables to determine state
    i = 0
    index = 0
    current_index = 0
    character_count = 0
    dot = False
    last_index = len(input_string) - 1
    state = "accepted"
    previous = "q"


    while i < len(input_string) and state == "accepted":
        previous_char, num[i], index, state = check_state(previous, input_string[i], i, last_index)
        i= i + 1

        if state != "accepted":
           print("sorry that is not a java floating point literal")
           break

    return try_again()


def check_state(previous, character, index, last):
    # Dictionary of accept states
    accept_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9, ".": "."}
    accept_chars = {"+": "+", "-": "-", "e": "E"}
    accept_EXT = {"f": "f", "F": "F"}

    if character in accept_nums and pre:
        return accept_chars[character], index, "accepted"
    elif character == "_" and index != 0:
        return "", index, "accepted"
    elif character in accept_chars and index != 0:
        return accept_chars[character], index, "accepted"
    elif character in accept_EXT and index == last:
        return 0, index, "accepted"
    else:
        return 0, index, "not accepted"

    return "not accepted"



#Dfa for accepting only 001+00101001
dfa={0:{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                   "7": 7, "8": 8, "9": 9, ".": ".", "_": "_"},
       1:{"e": "E"},
       2:{"+": "+", "-": "-", "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
          "6": 6, "7": 7, "8": 8, "9": 9},
       3:{"f": "f", "F": "F"}



def accepts(transitions,initial,accepting,s):
    state = initial
    try:
        for c in s:
            state = transitions[state][c]
        if(state in accepting):
            return 'Accepted'
        else:
            return 'Rejected'
    except:
        return 'Rejected'
print('Dfa of 101+ ',accepts(dfa,0,{3},'10101111000')) #Accepted

print('Dfa of 001+ ',accepts(dfa,0,{3},'00101010101')) #Accepted



if __name__ == '__main__':
    again = True
    while again:
        user_input = input('Please enter your floating point literal: ')
        again = main(user_input)
