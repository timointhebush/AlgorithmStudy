def solution(number, k):
    answer = []
    for n in number:
        while len(answer) > 0 and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)
    if k > 0:
        return "".join(answer[:-k])
    else:
        return "".join(answer)


if __name__ == "__main__":
    print(solution("4177252841", 4))
