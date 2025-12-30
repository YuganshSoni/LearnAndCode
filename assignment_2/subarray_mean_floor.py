from typing import List
FIRST_STRING_ELEMENTS = 2

def compute_prefix_sums(values: List[int]) -> List[int]:
    prefix_sums = [0]
    running_total = 0
    for value in values:
        running_total += value
        prefix_sums.append(running_total)
    return prefix_sums

def compute_floor_mean(prefix_sums: List[int], left: int, right: int) -> int:
    elements_sum = prefix_sums[right] - prefix_sums[left - 1]
    elements_count = right - left + 1
    return elements_sum // elements_count

def is_valid_query(left: int, right: int, size: int) -> bool:
    return 1 <= left <= right <= size

def take_input(user_message:str) -> List[int]:
    return list(map(int, input(user_message).split()))

def validate_number_count(numbers:list, size:int)->bool:
    if len(numbers) != size:
        print("Invalid input")
        return True
    return False

def take_index_strings_input(query_count: int, array_size: int):
    index_store = []
    for count in range(query_count):
        query = take_input(f"Enter {count} query : ")
        if validate_number_count(query, 2):
            continue

        left, right = query
        if not is_valid_query(left, right, array_size):
            continue

        index_store.append((left, right))
    return index_store
        
def main() -> None:
    array_size_and_query_information = take_input("Enter array size and number of queries : ")
    if validate_number_count(array_size_and_query_information, FIRST_STRING_ELEMENTS):
        return
    
    array_size, query_count = array_size_and_query_information
    array_values = take_input("Enter array elements : ")
    if validate_number_count(array_values, array_size) or array_size == 0:
        return

    prefix_sums = compute_prefix_sums(array_values)
    queries = take_index_strings_input(query_count, array_size)
    for query in queries:
        left_index, right_index = query
        print(compute_floor_mean(prefix_sums, left_index, right_index))

if __name__ == "__main__":
    main()
