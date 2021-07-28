def solution(s):
    answer = 0
    n = len(s)
    bracket = { 
        "(":0, "[":1, "{":2,
        ")":3, "]":4, "}":5
    }
    for i in range (n):
        idx = i
        stack = []
        proper = True
        for j in range(n):
            if bracket[s[idx]] >= 3:
                if len(stack) != 0 and bracket[stack[-1]] == bracket[s[idx]]-3:
                    stack.pop()
                else:
                    proper = False
                    break
            else:
                stack.append(s[idx])
            idx = (idx+1) % n
        if len(stack) != 0:
            proper = False
        if proper:
            answer += 1
    return answer

print(solution("[](){}"	))
print(solution("}]()[{"	))
print(solution("[)(]"	))
print(solution("}}}"	))
print(solution("{{{}"))