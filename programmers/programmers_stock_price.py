def solution(prices):
    n = len(prices)
    answer = [0 for i in range(n)]
    stack = [0]
    for idx in range(1, n):
        if prices[stack[-1]] <= prices[idx]:
            stack.append(idx)
        else:
            while stack and prices[stack[-1]] > prices[idx]:
                drop_idx = stack.pop()
                answer[drop_idx] = idx - drop_idx
            stack.append(idx)
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
    return answer

print(solution([1, 2, 3, 2, 3]))