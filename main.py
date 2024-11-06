from typing import List

# even_list의 스켈레톤 코드
def even_list(int_list: List[int]) -> List[int]:
    """
    숫자가 짝수인지 확인하고 짝수 리스트를 반환합니다.

    Args:
        int_list: 정수 리스트.

    Returns:
        짝수 정수의 리스트.
    """
    # TODO: even_list 구현
    return [num for num in int_list if num % 2 == 0]

# sum_of_squares_of_even의 스켈레톤 코드
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    리스트의 모든 짝수 숫자의 제곱합을 계산합니다.

    Args:
        even_int_list: 짝수 정수 리스트.

    Returns:
        리스트 내 모든 짝수 숫자의 제곱합.
    """
    # TODO: sum_of_squares_of_even 구현
    pass

# 메인 함수
def main():
    # 예제 리스트
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# 기본 코드
if __name__ == "__main__":
    main()
