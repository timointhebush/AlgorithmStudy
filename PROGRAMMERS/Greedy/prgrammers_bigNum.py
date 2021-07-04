def solution(number, k):
    answer = ""
    number = list(number)
    n = len(number)
    maxNum = int(max(number))
    find = False
    for left in range(n-k, 0, -1):
        if n == left:
            for num in number:
                answer += num
            break
        for cipher in range(maxNum, -1, -1):
            for search in range(n-left+1):
                if number[search] == str(cipher): 
                    answer += number[search]
                    number = number[search+1:]
                    n = n-search-1
                    find = True
                    break
            if find==True:
                break
        find = False
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))