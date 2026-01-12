from config import  NumberConfig
import random

def number_is_in_range(number:int, lower_limit:int, upper_limit:int)->bool:
    return number >=lower_limit and number <= upper_limit


def user_guess(user_message:str)->int:
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
    number_of_guesses = 0
    correct_guess = False

    while not correct_guess:
        input_number = user_guess(user_message=f"Guess a number between {LOWER_LIMIT} and {UPPER_LIMIT} : ")

        if not number_is_in_range(input_number, LOWER_LIMIT, UPPER_LIMIT):
            print("I will not count this one please enter a number in given range \n")
            continue

        number_of_guesses += 1

        if input_number==target_number:
            print("You guessed it in", number_of_guesses, "guesses.")
            correct_guess = True
        else:
            print("Too low, Guess again" if input_number < target_number else "Too high, guess again")

if __name__ == "__main__":
    main()


    