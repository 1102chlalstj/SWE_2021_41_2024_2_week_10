from typing import List

def even_list(int_list: List[int]) -> List[int]:
    # TODO: even_list 함수 구현
    return [num for num in int_list if num % 2 == 0]

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    # TODO: sum_of_squares_of_even 함수 구현
    pass

def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()