def solution(number, k):
    splitted_num_list = [int(n) for n in number]
    ordered_splitted_num_list = sorted(splitted_num_list)

    for ki in range(k):
        remove_target_num = ordered_splitted_num_list[ki]
        number = number.replace(str(remove_target_num), "", 1)
    return number


if __name__ == "__main__":
    print(solution("4177252841", 4))
