def solution(number, k):
    stack = [number[0]]
    if len(number) != 1:
        for num in number[1:]:
            while len(stack) > 0 and stack[-1] < num and k > 0:
                k -= 1
                stack.pop()
            stack.append(num)
        if k != 0:
            stack = stack[:-k]
    return "".join(stack)

print(solution("7654321", 4))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
