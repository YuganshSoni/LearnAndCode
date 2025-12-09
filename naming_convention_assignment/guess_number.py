from config import  NumberConfig
import random

def number_in_range(number:int, lower_limit:int, upper_limit:int)->bool:
    if number >=lower_limit and number <= upper_limit:
        return True
    return False

def take_input_number(user_message:str)->int:
    while True:
        try:
            input_number = int(input(user_message))
            return input_number
        except Exception as error :
            print("Please enter a valid Integer :", str(error))

def main():
    LOWER_LIMIT = NumberConfig.GUESS_NUMBER_LOWER_LIMIT
    UPPER_LIMIT = NumberConfig.GUESS_NUMBER_UPPER_LIMIT
    target_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number_of_guess = 0
    correct_guess = False

    while not correct_guess:
        input_number = take_input_number(user_message="Guess a number between 1 and 100 : ")

        if not number_in_range(input_number, LOWER_LIMIT, UPPER_LIMIT):
            input_number = take_input_number(user_message="I will not count this one please enter a number between 1 and 100 : ")
            continue

        number_of_guess += 1

        if input_number==target_number:
            print("You guessed it in", number_of_guess, "guesses.")
            correct_guess = True
        else:
            print("Too low, Guess again" if input_number < target_number else "Too high, guess again")

if __name__ == "__main__":
    main()


    