import random

def is_digit(digit : int):
    if '0' <= digit <='9':
        return True
    return False

def check_range(lower_bound : int, upper_bound: int, number: int):
    if is_digit(number) and lower_bound<= int(number) <=upper_bound:
        return True
    else:
        return False

def main():
    target_number = random.randint(1,100)
    success = False
    guess = input("Guess a number between 1 and 100 : ")
    number_of_guess = 0
    while not success:
        if not check_range(lower_bound=1, upper_bound=100, number=guess):
            guess=input("I will not count this one Please enter a number between 1 to 100")
            continue
        else:
            number_of_guess+=1
            guess=int(guess)

        if guess<target_number:
            guess=input("Too low. Guess again")
        elif guess>target_number:
            guess=input("Too High. Guess again")
        else:
            print("You guessed it in",number_of_guess,"guesses!")
            success=True


if __name__ == "__main__":
    main()