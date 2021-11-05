def solution(test_case):
    bulbs = input().split(" ")
    A, B = int(bulbs[0]), int(bulbs[1])
    C, D = int(bulbs[2]), int(bulbs[3])
    ans = 0
    if B <= C:
        ans = 0
    else:
        if D <= B:
            ans = int(D - C)
        else:
            ans = int(B - C)
    print("#{0} {1}".format(test_case, ans))


test_cases = int(input())
for _ in range(test_cases):
    solution(_)
