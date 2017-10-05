###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match- ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!
import random
def get_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("What is your guess?"))

def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def compare(digits, guess):
    clues = []
    if digits == guess:
        return '######## YOU DID IT!!!!!! ########'

    for i ,num in enumerate(digits):
        if num == guess[i]:
            clues.append('Match')
        elif num in guess:
            clues.append('Close')
        else:
            clues.append('Nope') 

    return clues
clues = []
code = generate_code()
while clues != '######## YOU DID IT!!!!!! ########':
    guess = get_guess()
    clues = compare(code, guess)
    print (clues)
