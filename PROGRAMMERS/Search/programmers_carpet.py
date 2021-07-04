def solution(brown, yellow):
    total = brown + yellow
    height = 3
    while total/height >= height:
        if total % height == 0:
            if (total/height - 2) * (height - 2) == yellow:
                return [int(total/height), height ]
        height += 1


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))