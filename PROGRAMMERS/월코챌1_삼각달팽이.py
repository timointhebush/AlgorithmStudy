def solution(n):
    answer = []
    global last
    last = 0
    for i in range(1, n + 1):
        last += i
    pyramid = [[] for _ in range(n + 1)]
    right_side = []
    cover_side(1, n, 1, pyramid, right_side)
    while right_side:
        idx_range, side = right_side.pop()
        for i in range(idx_range[0], idx_range[1] + 1):
            pyramid[i].append(side.pop())
    for i in range(1, n + 1):
        answer += pyramid[i]
    return answer


def cover_side(a, b, top, pyramid, right_side):
    if top == last:
        pyramid[a].append(top)
        return 0
    for i in range(a, b + 1):
        pyramid[i].append(top + (i - a))
    left_bottom = top + (b - a)
    right_bottom = left_bottom + (b - a)
    for i in range(left_bottom + 1, right_bottom):
        pyramid[b].append(i)
    if right_bottom == last:
        pyramid[b].append(last)
        return 0
    right_top = right_bottom + (b - a) - 1
    right_side.append(((a + 1, b), [i for i in range(right_bottom, right_top + 1)]))
    if right_top != last:
        cover_side(a + 2, b - 1, right_top + 1, pyramid, right_side)


print(solution(4))
print(solution(5))
print(solution(6))
