def calculate_armstrong_sum(number: int)->int:
    digits = str(number)
    digit_count = len(digits)
    return sum(int(digit) ** digit_count for digit in digits)

def is_armstrong_number(number:int)->bool:
    if number < 0:
        return False
    return number == calculate_armstrong_sum(number)

if __name__ == "__main__":  
    input_number = int(input("Please Enter the Number to Check for Armstrong: "))
    if is_armstrong_number(input_number):
        print(f"{input_number} is Armstrong Number.\n")
    else:
        print(f"{input_number} is Not a Armstrong Number.\n")
