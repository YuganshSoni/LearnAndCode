import random
from config import NumberConfig

def roll_dice(upper_limit:int)->int:
    return random.randint(1, upper_limit)

def main():
    dice_faces = NumberConfig.DICE_FACES
    while True:
        user_input = input("Press Enter to roll the dice, Enter Q to Quit : ")
        if user_input.lower() == NumberConfig.EXIT_COMMAND:
            break
        random_number = roll_dice(dice_faces)
        print("You have rolled a", random_number)

if __name__ == "__main__":
    main()