def solution(money):
    a = [0 for _ in range(len(money))]
    a[1] = money[1]
    for i in range(2, len(money)):
        a[i] = max(a[i - 1], money[i] + a[i - 2])

    b = [0 for _ in range(len(money))]
    b[0], b[1] = money[0], money[0]
    for i in range(2, len(money) - 1):
        b[i] = max(b[i - 1], money[i] + b[i - 2])
    return max(a[len(money) - 1], b[len(money) - 2])


print(solution([1, 2, 3, 1]))
