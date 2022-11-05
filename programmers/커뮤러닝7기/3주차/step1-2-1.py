def add_numbers(numbers, left_numbers, right_numbers):
    for left_num in left_numbers:
        for right_num in right_numbers:
            numbers.add(left_num + right_num)
            numbers.add(left_num - right_num)
            numbers.add(left_num * right_num)
            if right_num != 0:
                numbers.add(left_num // right_num)


def solution(N, number):
    answer = -1
    numbers_by_N_count = [{int(str(N) * i)} if i != 0 else {} for i in range(9)]

    for count in range(1, 9):
        for left_count in range(1, count):
            left_numbers = numbers_by_N_count[left_count]

            right_count = count - left_count
            right_numbers = numbers_by_N_count[right_count]

            add_numbers(numbers_by_N_count[count], left_numbers, right_numbers)
        if number in numbers_by_N_count[count]:
            answer = count
            break
    return answer


if __name__ == "__main__":
    print(solution(5, 12))
    print(solution(2, 11))