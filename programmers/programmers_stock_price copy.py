def solution(prices):
    answer = []
    n = len(prices)
    for price_idx in range(n):
        count = 0
        for compare_idx in range(price_idx+1, n):
            count += 1
            if prices[price_idx] > prices[compare_idx]:
                break
        answer.append(count)
    return answer

print(solution([1, 2, 3, 2, 3]))