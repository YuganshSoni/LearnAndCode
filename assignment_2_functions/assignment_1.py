import random

LOWER_BOUND = 1
UPPER_BOUND = 100

def is_within_range(number: int, lower: int, upper: int) -> bool:
    return lower <= number <= upper

def get_valid_guess(lower: int, upper: int) -> int:
    while True:
        try:
            user_input = int(input(f"Guess a number between {lower} and {upper}: "))
            if user_input is None:
                print("Please enter a valid input number")
                continue
            if not is_within_range(user_input, lower, upper):
                continue
            return user_input
        except Exception:
            print("Please enter a valid input number")
            continue

def play_game() -> None:
    target_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts = 0

    while True:
        guess = get_valid_guess(LOWER_BOUND, UPPER_BOUND)
        attempts += 1
        if guess < target_number:
            print("Guess a higher number")
        elif guess > target_number:
            print("Guess a lower number")
        else:
            print(f"You guessed number in {attempts} attempts")
            break

def main() -> None:
    play_game()

if __name__ == "__main__":
    main()