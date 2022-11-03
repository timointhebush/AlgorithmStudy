def solution(numbers):
    str_numbers = list(map(modify_number_to_extended_str, numbers))
    str_numbers = sorted(str_numbers, reverse=True)
    str_numbers = list(map(shorten, str_numbers))
    return "".join(str_numbers)


def modify_number_to_extended_str(number: int):
    return str(number) * 4


def shorten(str_number: str):
    tmp = int(len(str_number) / 4)
    return str_number[0:tmp]


if __name__ == "__main__":
    # print(solution([0, 10, 11, 12, 100]))
    # print(solution([3, 30, 34, 5, 9]))
    print(solution([0, 0, 0, 0]))