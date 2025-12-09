def calculate_armstrong_sum(number: int):
    armstrong_sum = 0
    digit_count = 0
 
    temp_number = number
    while temp_number > 0:
        digit_count = digit_count + 1
        temp_number = temp_number // 10
 
    temp_number = number
    for _ in range(1, temp_number + 1):
        digit = temp_number % 10
        armstrong_sum = armstrong_sum + (digit ** digit_count)
        temp_number //= 10
    return armstrong_sum


if __name__ == "__main__":  
    input_number = int(input("Please Enter the Number to Check for Armstrong: "))
    if (input_number == calculate_armstrong_sum(input_number)):
        print(f"{input_number} is Armstrong Number.\n")
    else:
        print(f"{input_number} is Not a Armstrong Number.\n")
