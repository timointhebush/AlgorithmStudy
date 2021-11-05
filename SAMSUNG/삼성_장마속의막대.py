def solution(test_case):
    tmp = input().split(" ")
    a, b = int(tmp[0]), int(tmp[1])
    m = int(b - a - 1)
    k = length_stick(m) - a
    print("#{0} {1}".format(test_case + 1, k))


def length_stick(x):
    length = 0
    for _ in range(x, 0, -1):
        length += _
    return length


test_cases = int(input())
for _ in range(test_cases):
    solution(_)
