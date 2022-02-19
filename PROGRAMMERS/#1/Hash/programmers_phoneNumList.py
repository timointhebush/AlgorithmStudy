def solution(phone_book):
    answer = True
    dict_phone_book = {}
    for phone_num in phone_book:
        dict_phone_book[phone_num] = 1
    for phone_num in phone_book:
        tmp = ""
        for num in phone_num:
            tmp += num
            if tmp in dict_phone_book and tmp != phone_num:
                answer = False
    return answer

print(solution(['119', '97674223', '1195524421']))