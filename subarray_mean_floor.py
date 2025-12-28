
def get_numbers_from_string(input_string:str):
    array = []
    current_number = 0
    is_digit = False

    for character in input_string:
        if '0' <= character <= '9':
            current_number = current_number * 10 + (ord(character) - ord('0'))
            is_digit = True
        else:
            if is_digit:
                array.append(current_number)
                current_number = 0
                is_digit = False
    if is_digit:
        array.append(current_number)

    return array

def get_numbers(input_string:str):
    array = get_numbers_from_string(input_string)
    return array[0], array[1]

def calculate_sum(left_limit:int, right_limit:int, number_array:list):
    sum = 0
    for index in range(left_limit-1, right_limit):
        sum += number_array[index]
    return sum

def get_sum(left_limit:int, right_limit:int, number_array:list):
    return calculate_sum(left_limit, right_limit, number_array)

def calculate_floor_mean(left_limit:int, right_limit:int, number_array:list)->int:
    sum_of_numbers = get_sum(left_limit, right_limit, number_array)
    total_number = right_limit - left_limit + 1
    return sum_of_numbers//total_number

def get_floor_mean_in_range(left_limit:int, right_limit:int, number_array:list)->int:
    return calculate_floor_mean(left_limit, right_limit, number_array)

def validate_range(left_limit:int, right_limit:int, array_size:int):
    if left_limit < 0 or right_limit > array_size:
        return False
    return True

def take_input():
    input_string = input("Enter number of array element and number of queries : ")
    array_size, number_of_queries = get_numbers(input_string)
    input_string = input("Enter array elements : ")
    number_array = get_numbers_from_string(input_string)

    while number_of_queries:
        input_string = input("Enter left and right index range : ")
        left_limit, right_limit = get_numbers(input_string)
        valid_range = validate_range(left_limit, right_limit, array_size)
        if not valid_range:
            print("Invalid range")
            continue
        floor_mean = get_floor_mean_in_range(left_limit, right_limit, number_array)
        print(floor_mean, end="\n")
        number_of_queries-=1

def main():
    take_input()

if __name__ == "__main__":
    main()